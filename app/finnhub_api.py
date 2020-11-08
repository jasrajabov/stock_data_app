import requests
from stockapp.settings import finnhub_api_key
from .utils import unixTimeConverter
# import ipdb; ipdb.set_trace()


class FinnhubApiMethods():

    def getStockQuote(stock_symbol, api_key=finnhub_api_key):
        url = 'https://finnhub.io/api/v1/quote?symbol={}&token={}'.format(
            stock_symbol, api_key)
        response = requests.get(url)
        # import ipdb; ipdb.set_trace()
        if response.json().get('t') == 0:
            return 'Incorrect Value'
        if response.json().get('s') == 'no_data':

            return 'Bad connection'
        return response.json()

    def getRecommendationTrends(stock_symbol, api_key=finnhub_api_key):
        url = 'https://finnhub.io/api/v1/stock/recommendation?symbol={}&token={}'.format(stock_symbol, api_key)
        response = requests.get(url)
        return response.json()

    def getPeers(stock_symbol, api_key=finnhub_api_key):
        url = 'https://finnhub.io/api/v1/stock/peers?symbol={}&token={}'.format(stock_symbol, api_key)
        response = requests.get(url)
        return response.json()

    def getCompanyProfile(stock_symbol, api_key=finnhub_api_key):
        url = 'https://finnhub.io/api/v1/stock/profile2?symbol={}&token={}'.format(stock_symbol, api_key)
        response = requests.get(url)
        return response.json()

    def getCandlestick(stock_symbol, api_key=finnhub_api_key, starttime=None):
        periods = unixTimeConverter(starttime)
        # import ipdb; ipdb.set_trace()
        url = 'https://finnhub.io/api/v1/stock/candle?symbol={}&resolution=5&from={}&to={}&token={}'.format(
            stock_symbol, periods[1], periods[0], api_key
        )
        response = requests.get(url)
        # import ipdb; ipdb.set_trace()
        return response.json()
