from django.urls import path
from . import views

urlpatterns = [
    path('porfile/', views.user_info),
    # GET: 프로필 조회, PUT: 프로필 수정
    path('deposits/<group_type>/', views.deposits_recommend),
    # group_type: age, monthly_income, assets, likes
    path('savings/<group_type>/', views.savings_recommend),

    path('travel/<save_period>', views.travel_recommand)
    # GET : 저축 기간에 따른 여행지 추천
]
