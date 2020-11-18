from django.test import TestCase, RequestFactory, Client
from django.urls import reverse, resolve
from django import urls
from app.finnhub_api import FinnhubApiMethods as fb
from stockapp.settings import finnhub_api_key
import requests
import requests_mock
from pytest_django.asserts import assertTemplateUsed
from app.views import *
import json
import pytest


def client_request(url):
    return Client().get(url)



class TestWithPytest:

    @pytest.mark.parametrize('param', [
        ('index'),
        ('fixinput'),
        ('fixvalidator')
    ])
    def test_views(self, param):
        url = urls.reverse(param)
        response = client_request(url)
        assert response.status_code == 200

    def test_home_gape(self):
        url = reverse('index')
        response = client_request(url)
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
        url = 'http://localhost:8000/fixvalidate/result?message_type=New+Order+Single&fix_message_to_validate=8=TEST'
        url2 = 'http://localhost:8000/fixvalidate/result?message_type=Order+Cancel+Request&fix_message_to_validate=8=TEST'
        response = client_request(url)
        response2 = client_request(url2)
        assert response.status_code == 200
        assert response2.status_code == 200
        assertTemplateUsed(response, 'fix_data_validator.html')
