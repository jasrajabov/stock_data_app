import requests
import requests_mock

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

def getCandlestick(stock_symbol, api_key=finnhub_api_key,debug_mode=None):
    url = sefl.url+'candle?symbol={}&resolution=1&from=1572651390&to=1572910590&token={}'.format(
        stock_symbol, api
    )
import datetime
from datetime import timedelta
myDate = '2020-01-04'
timestamp = datetime.datetime.strptime(myDate, "%Y-%m-%d").timestamp()
print(str(int(timestamp)))


t = datetime.datetime(2020,1,4).timestamp()
now = datetime.datetime.now()

day7ago = int((now - timedelta(days=7)).timestamp()).__str__()


print(t)
print(now)
print(day7ago)
