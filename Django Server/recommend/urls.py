from django.urls import path
from . import views

urlpatterns = [
    path('porfile/', views.user_info),
    # GET: 프로필 조회, PUT: 프로필 수정
    path('deposits/<group_type>/', views.deposits_recommend),
    # group_type: age, monthly_income, assets, likes
    path('savings/<group_type>/', views.savings_recommend),
]
