from django.urls import reverse, resolve


class TestUrls:

    def test_index_url(self):
        path = reverse('index')
        assert resolve(path).url_name == 'index'

    def test_stockdata_url(self):
        path = reverse('stockdata')
        assert resolve(path).view_name == 'stockdata'

    def test_candlestick_url(self):
        path = reverse('candelestick')
        assert resolve(path).view_name == 'candelestick'
