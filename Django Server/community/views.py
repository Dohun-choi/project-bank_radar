from datetime import datetime, timedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from django.db.models import Count
from django.db.models import Q


from .models import Post, Comment, Notify
from .serializers import PostListSerializer, PostSerializer, NestedCommentSerializer, NotifySerializer


def create_notify(post_user, post_pk, parent_user, data, writer_pk):
    if writer_pk != post_user.pk:
        Notify.objects.create(user=post_user, content=data, id_of_content=post_pk)
    if parent_user is not None and parent_user.pk != writer_pk:
        Notify.objects.create(user=parent_user, content=data, id_of_content=post_pk)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def posts(request):
    if request.method == 'GET':
        one_year_ago = (datetime.now() - timedelta(days=365)).strftime('%Y-%m-%d')

        posts = Post.objects.filter(created_at__gte=one_year_ago)
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data, context={'request':request})
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail(request, post_pk):
    post = get_object_or_404(Post.objects.prefetch_related('comment_set').order_by('-pk'), pk=post_pk)

    if request.method == 'GET':
        serializer = PostSerializer(post, context={'request':request})
        return Response(serializer.data)

    if post.user.id != request.user.id:
        return Response({'detail':'다른 사람이 작성한 게시글을 수정 또는 삭제할 수 없습니다.'})
    
    if request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data, partial=True, context={'request':request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


# @api_view(['GET'])
# def comments(request, post_pk):
#     post = get_object_or_404(Post, pk=post_pk)
#     comment = get_list_or_404(Comment, post=post)
#     serializer = CommentSerializer(comment, many=True)
#     return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request, post_pk):
    serializer = NestedCommentSerializer(data=request.data, context={'request':request})
    if serializer.is_valid(raise_exception=True):
        post = Post.objects.get(pk=post_pk)
        serializer.save(post=post, user=request.user)
        if serializer.data['parent'] is None:
            parent_user = None
        else:
            comment = get_object_or_404(Comment, pk=serializer.data['parent'])
            parent_user = comment.user
            print(parent_user)
        create_notify(post.user, post_pk, parent_user, request.data['content'], request.user.pk)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        # serializer = CommentSerializer(comment)
        # return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if comment.user.id != request.user.id:
        return Response({'detail':'다른 사람이 작성한 댓글을 수정 또는 삭제할 수 없습니다.'}, status=status.HTTP_401_UNAUTHORIZED)
    
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = NestedCommentSerializer(comment, data=request.data, context={'request':request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_like(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    is_liked = post.like_users.filter(pk=request.user.pk).exists()
    if is_liked:
        post.like_users.remove(request.user)
    else:
        post.like_users.add(request.user)
            
    like_count = post.like_users.aggregate(count=Count('id'))['count']

    data = {
        'isLiked': not is_liked,
        'likeCount': like_count
    }
    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_like(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    is_liked = comment.like_users.filter(pk=request.user.pk).exists()
    if request.user in comment.like_users.all():
        comment.like_users.remove(request.user)
    else:
        comment.like_users.add(request.user)
    like_count = comment.like_users.aggregate(count=Count('id'))['count']
    
    data = {
        'isLiked': not is_liked,
        'likeCount': like_count
    }
    return Response(data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def get_notifies(request):
    notifies = Notify.objects.filter(user=request.user)
    for notify in notifies:
        if not notify.read:
            notify.read = True
            notify.save()
    serializer = NotifySerializer(notifies, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def is_notify(request):
    notifies = Notify.objects.filter(user=request.user, read=False).count()
    return Response({'notifies': notifies})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_notify(request, notify_pk):
    notify = get_object_or_404(Notify, pk=notify_pk)
    notify.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_search(request):
    query = request.GET.get('search_query')
    print(query)

    if query:
        matching_posts = Post.objects.filter(
    Q(title__icontains=query) | Q(content__icontains=query)
)
        serializer = PostListSerializer(matching_posts, many=True)

        return Response(serializer.data)

    return Response([])


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def popular_posts(request):
    if request.method == 'GET':
        popular_in_month = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

        posts = Post.objects.filter(created_at__gte=popular_in_month) \
                    .annotate(num_likes=Count('like_users')) \
                    .order_by('-num_likes')
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)