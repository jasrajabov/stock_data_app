from django.test import TestCase, RequestFactory, Client
from django.urls import reverse, resolve
from app.finnhub_api import FinnhubApiMethods as fb
from stockapp.settings import finnhub_api_key
import requests
import requests_mock
from pytest_django.asserts import assertTemplateUsed
from app.views import *
import json


def client_request(url):
    return Client().get(url)

class TestWithPytest(TestCase):

    def test_home_gape(self):
        url = reverse('index')
        response = client_request(url)
        # request = RequestFactory().get(url)
        # response = stockData(request)
        print(response.templates[0])
        assert response.status_code == 200
        assertTemplateUsed(response, 'data.html')

    def test_home_gape_context(self):
        url = reverse('index')
        response = client_request(url)
        assert response.context['data']['company_profile']['ticker'] == 'GOOGL'

    def test_data_page(self):
        url = 'http://localhost:8000/data/?stock_symbol=AAPL'
        response = client_request(url)
        assert response.status_code == 200
        assertTemplateUsed(response, 'data.html')

    def test_search_invalid_stock_symbol(self):
        url = 'http://localhost:8000/data/?stock_symbol=123xyz'
        response = client_request(url)
        json_content = json.loads(response.content)
        assert response.status_code == 400
        assert json_content['Invalid']['stock_symbol'] == '123xyz'

    def test_fix_input_page(self):
        url = reverse('fixinput')
        response = client_request(url)
        assert response.status_code == 200
        assertTemplateUsed(response, 'fix_input.html')

    def test_fix_message_page(self):
        url = 'http://localhost:8000/fixmessage/?message_type=test&stock_symbol=test&quantity=1&side=Buy&order_type=test'
        response = client_request(url)
        # import ipdb; ipdb.set_trace()
        assert response.status_code == 200
        assertTemplateUsed(response, 'fix_data.html')

    def test_fix_validator_home_page(self):
        url = reverse('fixvalidator')
        response = client_request(url)
        assert response.status_code == 200
        assertTemplateUsed(response, 'fix_data_validator.html')

    def test_fixvalidator_result_page(self):
        url = 'http://localhost:8000/fixvalidate/result?message_type=New+Order+Single&fix_message_to_validate=test'
        response = client_request(url)
        assert response.status_code == 200
        assertTemplateUsed(response, 'fix_data_validator.html')
