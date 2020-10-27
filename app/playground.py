import requests
import requests_mock
from app.views import *

api_key = 'bu1sl5f48v6sao5m14jg'
response = requests.get('https://finnhub.io/api/v1/stock/peers?symbol=AAPL&token=bu1sl5f48v6sao5m14jg')
# print(response.status_code)
# print(response.text[0])


@requests_mock.Mocker()
def test_mock(mock):
    mock.get('https://finnhub.io/api/v1/stock/peers?symbol=AAPL&token=bu1sl5f48v6sao5m14jg', json={'a':'b'})
    response = requests.get('https://finnhub.io/api/v1/stock/peers?symbol=AAPL&token=bu1sl5f48v6sao5m14jg')
    # print(response.json())

##

import datetime
from datetime import timedelta
myDate = '2020-01-04'
timestamp = datetime.datetime.strptime(myDate, "%Y-%m-%d").timestamp()
print(str(int(timestamp)))

def getCandlestick(stock_symbol, api_key=finnhub_api_key, starttime=None):

    url = 'https://finnhub.io/api/v1/stock/candle?symbol={}&resolution=5&from={}&to={}&token={}'.format(
        stock_symbol, periods[1], periods[0], api_key
    )
    response = requests.get(url)
    # import ipdb; ipdb.set_trace()
    return response.json()
