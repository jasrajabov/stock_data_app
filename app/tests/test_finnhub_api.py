from django.test import TestCase, Client
from app.finnhub_api import FinnhubApiMethods as fb
from stockapp.settings import finnhub_api_key
import requests
import requests_mock
# import ipdb; ipdb.set_trace()

class TestFinnHubApi(TestCase):
    """
    Testing finnhub api
    """

    def setUp(self):
        self.stock_symbol = 'AAPL'
        self.incorrect_stock_symbol = '123xyz'
        self.api_key=finnhub_api_key

    def test_getStockQuote_postive_and_negative_data(self):
        response = fb.getStockQuote(self.stock_symbol)
        self.assertNotEqual(response.get('t'), 0)
        response2 = fb.getStockQuote(self.incorrect_stock_symbol)
        self.assertEqual(response2, 'Incorrect Value')

    def test_connectivity(self):
        url = 'https://finnhub.io/api/v1/quote?symbol={}&token={}'.format(self.stock_symbol, self.api_key)
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)

    @requests_mock.Mocker()
    def test_FinnhubApiMethods(self, mock):
        stock_quote_url = 'https://finnhub.io/api/v1/quote?symbol={}&token={}'.format(self.stock_symbol, self.api_key)
        mock.get(stock_quote_url, json={'a':'b'})
        rec_data_url = url = 'https://finnhub.io/api/v1/stock/recommendation?symbol={}&token={}'.format(self.stock_symbol, self.api_key)
        mock.get(rec_data_url, json={'c':'d'})
        peer_data_url = url = 'https://finnhub.io/api/v1/stock/peers?symbol={}&token={}'.format(self.stock_symbol, self.api_key)
        mock.get(peer_data_url, json={'e':'f'})

        self.assertEqual(fb.getStockQuote(self.stock_symbol, self.api_key), {'a':'b'})
        self.assertEqual(fb.getRecommendationTrends(self.stock_symbol, self.api_key), {'c':'d'})
        self.assertEqual(fb.getPeers(self.stock_symbol, self.api_key), {'e':'f'})
