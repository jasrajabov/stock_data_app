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
    print(response.json())

test_mock()    
