from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from django.shortcuts import get_list_or_404, get_object_or_404

from .models import Post, Comment
from .serializers import PostListSerializers, PostSerializers, CommntSerializer

# Create your views here.
@api_view(['GET', 'POST'])
def posts(reqeust):
    if reqeust.method == 'GET':
        posts = get_list_or_404(Post)
        serializer = PostListSerializers(posts, many=True)
        return Response(serializer.data)
    
    elif reqeust.method == 'POST':
        serializer = PostSerializers(data=reqeust.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'DELETE', 'PUT'])
def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)

    if request.method == 'GET':
        serializer = PostSerializers(post)
        return Response(serializer.data)


    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = PostSerializers(post, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
        
@api_view(['GET'])
def comments(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comment = get_list_or_404(Comment, post=post)
    serializer = CommntSerializer(comment, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def create_comment(request, post_pk):
    serializer = CommntSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        post = Post.objects.get(pk=post_pk)
        serializer.save(post=post)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
def comment_detail(request, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommntSerializer(comment)
        return Response(serializer.data)
    
    elif request.method == 'DELETE':
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    elif request.method == 'PUT':
        serializer = CommntSerializer(comment, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            return Response(serializer.data)