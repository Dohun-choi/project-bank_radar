from rest_framework import serializers
from .models import Post, Comment, Notify
from mptt.utils import tree_item_iterator

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'updated_at', )



# class CommentSerializer(serializers.ModelSerializer):
#     like_count = serializers.IntegerField(source='like_users.count', read_only=True)
#     is_liked = serializers.SerializerMethodField(method_name='has_liked', read_only=True)

#     class Meta:
#         model = Comment
#         fields = '__all__'
#         read_only_fields = ('user', 'like_users', 'post')
    
#     def has_liked(self, obj):
#         request = self.context.get('request')
#         if request and request.user.is_authenticated:
#             return obj.like_users.filter(id=request.user.id).exists()
#         return False
        

# class PostSerializer(serializers.ModelSerializer):
#     comment_set = CommentSerializer(many=True, read_only=True)
#     comment_count = serializers.IntegerField(source='comment_set.count', read_only=True)
#     like_count = serializers.IntegerField(source='like_users.count', read_only=True)
#     is_liked = serializers.SerializerMethodField(method_name='has_liked', read_only=True)

#     class Meta:
#         model = Post
#         fields = '__all__'
#         read_only_fields = ('user', 'like_users')

#     def has_liked(self, obj):
#         request = self.context.get('request')
#         if request and request.user.is_authenticated:
#             return obj.like_users.filter(id=request.user.id).exists()
#         return False

class NestedCommentSerializer(serializers.ModelSerializer):
    like_count = serializers.IntegerField(source='like_users.count', read_only=True)
    is_liked = serializers.SerializerMethodField(method_name='has_liked', read_only=True)
    children = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = fields = '__all__'
        read_only_fields = ('user', 'like_users', 'post')

    def get_children(self, obj):
        children = Comment.objects.filter(post=obj.post_id, parent=obj.id)
        serialized_children = self.__class__(children, many=True, context=self.context).data
        return serialized_children

    def has_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.like_users.filter(id=request.user.id).exists()
        return False

class PostSerializer(serializers.ModelSerializer):
    comment_set = serializers.SerializerMethodField(method_name='get_root_comments')
    like_count = serializers.IntegerField(source='like_users.count', read_only=True)
    is_liked = serializers.SerializerMethodField(method_name='has_liked', read_only=True)

    class Meta:
        model = Post
        fields = fields = '__all__'
        read_only_fields = ('user', 'like_users')

    def has_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.like_users.filter(id=request.user.id).exists()
        return False

    def get_root_comments(self, obj):
        root_comments = Comment.objects.filter(post=obj, parent__isnull=True)
        serializer = NestedCommentSerializer(root_comments, many=True, context=self.context)
        return serializer.data
    

class NotifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Notify
        fields = '__all__'
        exclude = ('user',)