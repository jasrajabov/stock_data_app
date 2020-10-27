from django.test import TestCase, Client
from app.finnhub_api import FinnhubApiMethods as fb
from stockapp.settings import finnhub_api_key
import requests
# import ipdb; ipdb.set_trace()

class TestFinnHubApi:
    """
    Testing finnhub api
    """

    stock_symbol = 'AAPL'
    incorrect_stock_symbol = '123xyz'
    api_key=finnhub_api_key
    client = Client()

    def test_getStockQuote_postive_and_negative_data(self):
        response = fb.getStockQuote(self.stock_symbol)
        assert response.get('t') != 0
        response2 = fb.getStockQuote(self.incorrect_stock_symbol)
        assert response2 == 'Incorrect Value'

    def test_connectivity(self):
        url = 'https://finnhub.io/api/v1/quote?symbol={}&token={}'.format(self.stock_symbol, self.api_key)
        response = requests.get(url)
        assert response.status_code == 200

    def test_FinnhubApiMethods(self, requests_mock):
        stock_quote_url = 'https://finnhub.io/api/v1/quote?symbol={}&token={}'.format(self.stock_symbol, self.api_key)
        requests_mock.get(stock_quote_url, json={'a':'b'})
        rec_data_url = 'https://finnhub.io/api/v1/stock/recommendation?symbol={}&token={}'.format(self.stock_symbol, self.api_key)
        requests_mock.get(rec_data_url, json={'c':'d'})
        peer_data_url = 'https://finnhub.io/api/v1/stock/peers?symbol={}&token={}'.format(self.stock_symbol, self.api_key)
        requests_mock.get(peer_data_url, json={'e':'f'})

        assert fb.getStockQuote(self.stock_symbol, self.api_key) == {'a':'b'}
        assert fb.getRecommendationTrends(self.stock_symbol, self.api_key) == {'c':'d'}
        assert fb.getPeers(self.stock_symbol, self.api_key) == {'e':'f'}
