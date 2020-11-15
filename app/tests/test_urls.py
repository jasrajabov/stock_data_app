from django.urls import reverse, resolve
from django.test import TestCase
from app.views import *

class TestUrls(TestCase):

    def test_index_url(self):
        path = reverse('index')
        _resolve = resolve(path)
        assert _resolve.url_name == 'index'
        assert _resolve.func == stockData

    def test_stockdata_url(self):
        path = reverse('stockdata')
        _resolve = resolve(path)
        assert resolve(path).view_name == 'stockdata'
        assert _resolve.func == stockData

    def test_fixinput_url(self):
        path = reverse('fixinput')
        _resolve = resolve(path)
        assert resolve(path).view_name == 'fixinput'
        assert _resolve.func == fix_input

    def test_fixmessage_url(self):
        path = reverse('fixmessage')
        _resolve = resolve(path)
        assert resolve(path).view_name == 'fixmessage'
        assert _resolve.func == generate_fix_message

    def test_fixvalidator_home_url(self):
        path = reverse('fixvalidator')
        _resolve = resolve(path)
        assert resolve(path).view_name == 'fixvalidator'
        assert _resolve.func == validate_fix_message_home

    def test_fixvalidator_result_url(self):
        path = reverse('fixvalidator_result')
        _resolve = resolve(path)
        assert resolve(path).view_name == 'fixvalidator_result'
        assert _resolve.func == validate_fix_message



    """
    path('', views.stockData, name='index'),
    path('data/', views.stockData, name='stockdata'),
    path('fixinput/', views.fix_input, name='fixinput'),
    path('fixmessage/', views.generate_fix_message, name='fixmessage'),
    path('fixvalidate/', views.validate_fix_message_home, name='fixvalidator'),
    path('fixvalidate/result', views.validate_fix_message, name='fixvalidator_result')
    """
