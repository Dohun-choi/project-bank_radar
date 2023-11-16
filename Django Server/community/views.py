from datetime import datetime, timedelta
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django.shortcuts import get_list_or_404, get_object_or_404
from django.db.models import Count

from .models import Post, Comment
from .serializers import PostListSerializer, PostSerializer, CommentSerializer


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def posts(request):
    if request.method == 'GET':
        one_year_ago = datetime.now() - timedelta(days=365)

        posts = get_list_or_404(Post.objects.filter(created_at__gte=one_year_ago))
        serializer = PostListSerializer(posts, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_detail(request, post_pk):
    post = get_object_or_404(Post.objects.prefetch_related('comment_set').order_by('-pk'), pk=post_pk)

    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)

    if post.user.id != request.user.id:
        return Response({'detail':'다른 사람이 작성한 게시글을 수정 또는 삭제할 수 없습니다.'})
    
    if request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data, partial=True)
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
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        post = Post.objects.get(pk=post_pk)
        serializer.save(post=post, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        # serializer = CommentSerializer(comment)
        # return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if comment.user.id != request.user.id:
        return Response({'오류':'다른 사람이 작성한 댓글을 수정 또는 삭제할 수 없습니다.'})
    
    if request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
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
