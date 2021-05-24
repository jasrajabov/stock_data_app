from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from app.finnhub_api import FinnhubApiMethods as fb
from app.utils import createChart, fix_splitter, fix_message_generator
from app.fix_engine import FixMessageGenerator, FixMessageValidator
import json
# from app.serializers import StockDataSerializer


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

    stock_json_data = fb.getStockQuote(stock_symbol)
    if stock_json_data == 'Incorrect Value':
        return JsonResponse({'Invalid':request.GET}, status=400)
    elif stock_json_data == 'Bad connection':
        return HttpResponse('Bad Connection', status=404)
    elif 'Failed to generate json!' in stock_json_data:
        return JsonResponse({'Error':stock_json_data}, status=400)
    rec_json_data = fb.getRecommendationTrends(stock_symbol)
    peers_json_data = fb.getPeers(stock_symbol)
    company_profile = fb.getCompanyProfile(stock_symbol)
    candle_stick_data = fb.getCandlestick(stock_symbol, starttime=start_time)
    plt_div = createChart(candle_stick_data, stock_symbol)
    data = {'quote':stock_json_data,
            'recommendation_trends':rec_json_data[:5],
            'peers':peers_json_data,
            'company_profile': company_profile}
    # import ipdb; ipdb.set_trace()
    return render(request, 'data.html', {'data':data, 'plot_div': plt_div},)


def fix_input(request):
    return render(request, 'fix_input.html', status = 200)


def generate_fix_message(request):
    data = request.GET
    message_type = request.GET['message_type']
    fix_message = fix_message_generator(data)
    if fix_message:
        splitted_fix = fix_splitter(fix_message, message_type)
        return render(request, 'fix_data.html', {'fix_message':fix_message,
                    'message_type':message_type,
                    'splitted_fix':splitted_fix},
            status=200)
    return JsonResponse({'invlid_data':'invalid message type'}, status=400)

def validate_fix_message_home(request):
    return render(request, 'fix_data_validator.html', status=200)

def validate_fix_message(request):
    fix_validator = FixMessageValidator()
    message_type = request.GET['message_type']
    fix_message = request.GET['fix_message_to_validate']
    validator_result = None
    value_errors = None
    if message_type == 'New Order Single':
        validator_result, value_errors = fix_validator.validate_new_order_request(fix_message)
    elif message_type == 'Order Cancel Request':
        validator_result, value_errors = fix_validator.validate_new_cancel_request(fix_message)
    return render(request, 'fix_data_validator.html',
    {
        'validator_result':validator_result,
        'value_errors': value_errors,
        'fix_message':fix_message
    },
    status=200)

def api(request):
    """
    This is to serve fix data in json format for post requests
    """
    data = request.POST
    if data != {}:
        fix_message = fix_message_generator(data)
        # return JsonResponse({'fix_message': fix_message})
        return HttpResponse({'fix_message': fix_message}, content_type='application/json')

    return HttpResponse({'error': 'no message provided'}, content_type='application/json')
