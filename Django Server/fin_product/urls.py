from django.urls import path
from . import views

urlpatterns = [
    path('update/', views.update_product), # 외부 API에서 환율 정보 가져오기
     # DB에서 가져오기
    path('deposits/', views.deposit_from_DB),
    path('savings/', views.saving_from_DB),
    # option 키에 옵션을 담아 함께 가져온다.
    path('deposits/debate/<str:fin_prdt_cd>/', views.deposit_debate),
    # 예금 토론(댓글) 가져오기
    path('savings/debate/<str:fin_prdt_cd>/', views.saving_debate),
    # 적금 토론(댓글) 가져오기
    path('deposits/<int:option_pk>/', views.deposit_intos),
    # 예금 좋아요
    path('savings/<int:option_pk>/', views.saving_intos),
    # 적금 좋아요
]
