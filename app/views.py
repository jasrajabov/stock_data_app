from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.finnhub_api import FinnhubApiMethods as fb
import json

def index(request):
    return render(request, 'home.html')

def stockData(request):
    stock_symbol =  request.GET['stock_symbol']
    # import ipdb; ipdb.set_trace()
    debug_mode = False if request.GET['debug_mode'] == 'false' else True

    stock_json_data = fb.getStockQuote(stock_symbol, debug_mode=debug_mode)
    if stock_json_data == 'Incorrect Value':
        return JsonResponse({'Invalid':request.GET}, status=404)
    rec_json_data = fb.getRecommendationTrends(stock_symbol, debug_mode=debug_mode)

    peers_json_data = fb.getPeers(stock_symbol, debug_mode=debug_mode)

    company_profile = fb.getCompanyProfile(stock_symbol, debug_mode=debug_mode)

    data = {'quote':stock_json_data,
            'recommendation_trends':rec_json_data[0],
            'peers':peers_json_data,
            'company_profile': company_profile
                        }
    return render(request, 'data.html', {'data':data})
