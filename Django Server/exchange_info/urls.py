from django.urls import path
from . import views

urlpatterns = [
    path('renew/', views.renew_exchange_info), # 외부 API에서 환율 정보 가져오기
    path('', views.exchange_from_DB) # DB에서 가져오기
]
