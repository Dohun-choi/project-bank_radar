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
    path('travel/<int:save_period>/', views.travel_recommand),
    # GET : 저축 기간에 따른 여행지 추천
    path('travel/<str:country>/', views.get_saving_for_travel)
    # GET : 여행지에 따른 적금상품 추천
]
