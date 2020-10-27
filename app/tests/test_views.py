from django.test import TestCase, RequestFactory
from app.finnhub_api import FinnhubApiMethods as fb
from stockapp.settings import finnhub_api_key
import requests
import requests_mock
from app.views import *


class TestWithPytest:


    def test_home_page(self):
        url = 'http://localhost:8000/data/?stock_symbol=AAPL&debug_mode=false'
        request = RequestFactory().get(url)
        response = index(request)

        assert response.status_code == 200

    def test_search_invalid_stock_symbol(self):

        url = 'http://localhost:8000/data/?stock_symbol=123xyz&debug_mode=false'
        request = RequestFactory().get(url)
        response = stockData(request)
        assert response.status_code == 404
