import requests

api_key = 'bu1sl5f48v6sao5m14jg'
response = requests.get('https://finnhub.io/api/v1/quote?symbol=AAPL&token=bu1sl5f48v6sao5m14jg')
print(response.status_code)
print(response.json())
