from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.user_info),
    # GET: 프로필 조회, PUT: 프로필 수정
    path('deposits/<str:group_type>/', views.deposits_recommend),
    path('savings/<str:group_type>/', views.savings_recommend),
    # group_type: age, monthly_income, assets, likes

    path('travel/', views.get_country),
    # GET: 등록된 여행지 목록
    path('travel/update/', views.get_img_url),
    # 네이버 이미지 검색 API로 나라별 사진 url 업데이트
    path('travel/<int:save_period>/', views.travel_recommand),
    # GET : 저축 기간에 따른 여행지 추천
    path('travel/<str:country>/', views.get_saving_for_travel),
    # GET : 여행지에 따른 적금상품 추천
    # params (선택 사항) - 없으면 옵션별 최대금액 납입 시의 만기 금액에 따라 추천
    # monthly_saving: 월 적금액
    # intr_rate_type: 복리 M, 단리 S <- 선택의 선택, 기본 값: 단리
    # period: 적금 기간
    # 월 적금액과 적금 기간을 고려한 상품 추천
    
]
