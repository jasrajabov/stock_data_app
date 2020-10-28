from django.test import TestCase, RequestFactory, Client
from django.urls import reverse, resolve
from app.finnhub_api import FinnhubApiMethods as fb
from stockapp.settings import finnhub_api_key
import requests
import requests_mock
from app.views import *


def client_request(url):
    return Client().get(url)

class TestWithPytest(TestCase):

    def test_home_gape(self):
        url = reverse('index')
        request = RequestFactory().get(url)
        response = stockData(request)
        assert response.status_code == 200

    def test_home_gape_context(self):
        url = reverse('index')
        response = client_request(url)
        assert response.context['data']['company_profile']['ticker'] == 'GOOGL'

    def test_data_page(self):
        url = 'http://localhost:8000/data/?stock_symbol=AAPL'
        request = RequestFactory().get(url)
        response = stockData(request)

        assert response.status_code == 200

    def test_search_invalid_stock_symbol(self):

        url = 'http://localhost:8000/data/?stock_symbol=123xyz'
        request = RequestFactory().get(url)
        response = stockData(request)
        assert response.status_code == 404
