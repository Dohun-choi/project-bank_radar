from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts),
    # GET: 최근 1년 게시글, POST: 새 글 쓰기
    path('posts/<int:post_pk>/', views.post_detail),
    # GET: 게시글 상세 + 댓글, DELETE: 게시글 삭제, PUT: 게시글 수정
    path('posts/<int:post_pk>/likes/', views.post_like),
    # POST: 게시글 좋아요/취소, 개수

    path('posts/<int:post_pk>/comments/', views.create_comment),
    # POST: 게시글에 댓글 달기
    # 대댓글: {parent: 대댓글 달려는 댓글의 id(pk)}
    # path('comments/<int:post_pk>/', views.comments),
    # GET: 해당 게시물의 댓글 조회
    path('comments/detail/<int:comment_pk>', views.comment_detail),
    # GET: 단일 댓글 조회, DELETE: 댓글 삭제, PUT: 댓글 수정
    path('comments/<int:post_pk>/likes/', views.comment_like),
    # POST: 댓글 좋아요/취소, 개수
]
