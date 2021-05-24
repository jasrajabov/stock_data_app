from django.urls import path
from app import views

urlpatterns = [

    path('', views.stockData, name='index'),
    path('data/', views.stockData, name='stockdata'),
    path('fixinput/', views.fix_input, name='fixinput'),
    path('fixmessage/', views.generate_fix_message, name='fixmessage'),
    path('fixvalidate/', views.validate_fix_message_home, name='fixvalidator'),
    path('fixvalidate/result', views.validate_fix_message, name='fixvalidator_result'),
    path('fixmessage/api', views.api, name='fix_server_api')

]
