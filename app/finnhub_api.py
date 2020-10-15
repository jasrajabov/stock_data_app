import requests
from stockapp.settings import finnhub_api_key
# import ipdb; ipdb.set_trace()


class FinnhubApiMethods():

    def getStockQuote(stock_symbol, api_key=finnhub_api_key, debug_mode=None):
        url = 'https://finnhub.io/api/v1/quote?symbol={}&token={}'.format(
            stock_symbol, api_key)
        if debug_mode == True:
            import ipdb; ipdb.set_trace()
        response = requests.get(url)
        if response.json().get('t') == 0:
            return 'Incorrect Value'
        return response.json()

    def getRecommendationTrends(stock_symbol, api_key=finnhub_api_key,debug_mode=None):
        url = 'https://finnhub.io/api/v1/stock/recommendation?symbol={}&token={}'.format(stock_symbol, api_key)
        response = requests.get(url)
        return response.json()

    def getPeers(stock_symbol, api_key=finnhub_api_key,debug_mode=None):
        url = 'https://finnhub.io/api/v1/stock/peers?symbol={}&token={}'.format(stock_symbol, api_key)
        response = requests.get(url)
        return response.json()
