from django.urls import path
from . import views

urlpatterns = [
    path('update/', views.update_product), # 외부 API에서 환율 정보 가져오기
     # DB에서 가져오기
    path('deposits/', views.deposit_from_DB),
    path('savings/', views.saving_from_DB),
    # option 키에 옵션을 담아 함께 가져온다.
]
