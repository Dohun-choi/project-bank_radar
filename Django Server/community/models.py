from django.db import models
from django.conf import settings
from mptt.models import MPTTModel, TreeForeignKey

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_post")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="post_writer", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# class Comment(models.Model):
#     post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_set')
#     content = models.CharField(max_length=150)
#     like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_comment")
#     user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comment_writer", on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class Comment(MPTTModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment_set')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    content = models.CharField(max_length=150)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="like_comment")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="comment_writer", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['created_at']