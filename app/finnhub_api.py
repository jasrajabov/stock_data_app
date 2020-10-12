import requests
from stockapp.settings import finnhub_api_key

def getStockQuote(stock_symbol, api_key=finnhub_api_key):
    url = 'https://finnhub.io/api/v1/quote?symbol={}&token={}'.format(stock_symbol, api_key)
    response = requests.get(url)
    return response.json()
