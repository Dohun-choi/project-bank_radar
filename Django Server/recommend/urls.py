from django.urls import path
from . import views

urlpatterns = [
    path('info/', views.user_info),
    path('deposits/', views.deposits_recommend),
    path('saivngs/', views.savings_recommend),
]
