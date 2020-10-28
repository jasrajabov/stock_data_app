from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.finnhub_api import FinnhubApiMethods as fb
from app.utils import createChart
import json


def index(request):
    # import ipdb; ipdb.set_trace()
    return render(request, 'home.html', status = 200)

def stockData(request):
    if request.path == '/':
        stock_symbol = 'GOOGL'
        start_time = '1'
    else:
        stock_symbol =  request.GET['stock_symbol']
        if 'date' in request.GET:
            start_time = request.GET['date']
        else:
            start_time = '1'

    # import ipdb; ipdb.set_trace()

    stock_json_data = fb.getStockQuote(stock_symbol)
    if stock_json_data == 'Incorrect Value':
        return JsonResponse({'Invalid':request.GET}, status=404)
    rec_json_data = fb.getRecommendationTrends(stock_symbol)
    peers_json_data = fb.getPeers(stock_symbol)
    company_profile = fb.getCompanyProfile(stock_symbol)
    candle_stick_data = fb.getCandlestick(stock_symbol, starttime=start_time)
    plt_div = createChart(candle_stick_data)

    data = {'quote':stock_json_data,
            'recommendation_trends':rec_json_data[0],
            'peers':peers_json_data,
            'company_profile': company_profile

                        }

    return render(request, 'data.html', {'data':data, 'plot_div': plt_div},)
