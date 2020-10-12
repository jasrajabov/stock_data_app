from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app import finnhub_api

def index(request):
    return render(request, 'home.html')

def stockData(request):
    stock_symbol =  request.GET['stock_symbol']
    stock_json_data = finnhub_api.getStockQuote(stock_symbol)
    return JsonResponse({'quote':stock_json_data})
