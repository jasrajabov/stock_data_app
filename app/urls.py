from django.urls import path
from app import views

urlpatterns = [

    path('', views.index, name='index'),
    path('data/', views.stockData, name='stockdata')

]
