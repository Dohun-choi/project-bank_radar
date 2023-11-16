from django.urls import path
from . import views

urlpatterns = [
    path('update/', views.update_exchange_DB), # 외부 API에서 환율 정보 가져오기
    path('', views.exchange_from_DB) # DB에서 가져오기
]
