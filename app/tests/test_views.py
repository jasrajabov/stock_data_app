from django.test import TestCase
from app.finnhub_api import FinnhubApiMethods as fb
from stockapp.settings import finnhub_api_key
import requests
import requests_mock
from app.views import stockData


class TestViews(TestCase):
    """Testing views"""

    def setUp(self):
        self.stock_symbol = 'AAPL'
        self.api_key=finnhub_api_key
        self.url = 'http://localhost:8000/data/?stock_symbol=AAPL&debug_mode=false'

    def test_home_page(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_search_invalid_stock_symbol(self):
        url = self.url = 'http://localhost:8000/data/?stock_symbol=123xyz&debug_mode=false'
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 404)
