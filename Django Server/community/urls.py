from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts),
    path('posts/<int:post_pk>/comments/', views.create_comment),
    path('posts/<int:post_pk>/', views.post_detail),
    path('comment/<int:post_pk>/', views.comments),
    path('comment/detail/<int:comment_pk>', views.comment_detail),
]
