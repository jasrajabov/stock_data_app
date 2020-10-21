from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.finnhub_api import FinnhubApiMethods as fb
import json
import pandas as pd
import plotly.graph_objects as go
from plotly.offline import plot

def index(request):
    return render(request, 'home.html')

def stockData(request):
    stock_symbol =  request.GET['stock_symbol']
    # import ipdb; ipdb.set_trace()

    stock_json_data = fb.getStockQuote(stock_symbol)
    if stock_json_data == 'Incorrect Value':
        return JsonResponse({'Invalid':request.GET}, status=404)
    rec_json_data = fb.getRecommendationTrends(stock_symbol)

    peers_json_data = fb.getPeers(stock_symbol)

    company_profile = fb.getCompanyProfile(stock_symbol)

    data = {'quote':stock_json_data,
            'recommendation_trends':rec_json_data[0],
            'peers':peers_json_data,
            'company_profile': company_profile
                        }
    return render(request, 'data.html', {'data':data})

def getCandlestickData(request):
    starttime = request.GET['date']
    stock_symbol =  request.GET['stock_symbol']
    candle_stick_data = fb.getCandlestick(stock_symbol, starttime=starttime)
    df = pd.DataFrame(candle_stick_data)
    # import ipdb; ipdb.set_trace()

    fig = go.Figure(data=[go.Candlestick(x=df['t'],
                    open=df['o'], high=df['h'],
                    low=df['l'], close=df['c'])
                         ])

    fig.update_layout(xaxis_rangeslider_visible=False,
                        autosize=False,
                        width=1000,
                        height=500,)
    plt_div = plot(fig, output_type='div')
    # fig.write_html("app/templates/_chart.html", include_plotlyjs=False, default_width='50%',
    #     full_html=False, include_mathjax=False)
    # # fig.show()

    return render(request, 'chart.html', context={'plot_div': plt_div})
