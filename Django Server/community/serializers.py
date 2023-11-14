from rest_framework import serializers
from .models import Post, Comment

class PostListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'updated_at', )

class PostSerializers(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

class CommntSerializer(serializers.ModelSerializer):

    class PostSerializer(serializers.ModelSerializer):
        class Meta:
            model = Post
            fields = ('id', 'title',)

    post = PostSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'
