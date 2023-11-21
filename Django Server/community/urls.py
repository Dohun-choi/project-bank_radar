from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.posts),
    # GET: 최근 1년 게시글, POST: 새 글 쓰기
    path('posts/popular/', views.popular_posts),
    # GET : 이번 달 작성된 인기 게시글 조회(좋아요 순서)
    path('posts/<int:post_pk>/', views.post_detail),
    # GET: 게시글 상세 + 댓글, DELETE: 게시글 삭제, PUT: 게시글 수정
    path('posts/<int:post_pk>/likes/', views.post_like),
    # POST: 게시글 좋아요/취소, 개수
    path('posts/search/', views.post_search),
    # GET: 요청 주소에 params : {search_query : '검색할 내용'} 추가하기

    path('posts/<int:post_pk>/comments/', views.create_comment),
    # POST: 게시글에 댓글 달기
    # 대댓글: {parent: 대댓글 달려는 댓글의 id(pk)}
    # path('comments/<int:post_pk>/', views.comments), 안씀
    # GET: 해당 게시물의 댓글 조회 안씀
    path('comments/detail/<int:comment_pk>/', views.comment_detail),
    # GET: 단일 댓글 조회(안씀), DELETE: 댓글 삭제, PUT: 댓글 수정
    path('comments/<int:comment_pk>/likes/', views.comment_like),
    # POST: 댓글 좋아요/취소, 개수

    path('notify/', views.get_notifies),
    # POST: 내 게시글에 달린 댓글, 댓글에 달린 대댓글 목록 불러오기
    # read 필드: 이 필드가 False인 알람이 불러와 진다.
    # id_of_content 필드: 알람이 발생된 게시글 pk
    # content 필드: 달린 댓글 또는 대댓글의 내용
    # 모든 알람의 read 필드를 True로 반환
    path('notify/<int:notify_pk>/', views.delete_notify),
    # DELETE: 알람 삭제
    path('isnotify/', views.is_notify),
    # GET: 안 읽은 알람 개수 반환 {'notifies': 알람 개수} 형태
]
