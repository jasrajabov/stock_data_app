from django.urls import path
from app import views

urlpatterns = [

    path('', views.stockData, name='index'),
    path('data/', views.stockData, name='stockdata'),
    path('fixinput/', views.fix_input, name='fixdata'),
    path('fixmessage/', views.generate_fix_message, name='fixmessage')
]
