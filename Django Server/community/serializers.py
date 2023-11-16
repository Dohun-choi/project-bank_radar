from rest_framework import serializers
from .models import Post, Comment


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'updated_at', )



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('user', 'like_users', 'post')
        

class PostSerializer(serializers.ModelSerializer):
    comment_set = CommentSerializer(many=True, read_only=True)
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
    like_count = comment_count = serializers.IntegerField(source='like_users.count', read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ('user', 'like_users')

