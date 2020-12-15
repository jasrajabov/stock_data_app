from django.test import TestCase
from app.utils import *
from unittest import mock



class TestUtils:

    def test_chart_with_no_data(self):
        chart = createChart({'s':'no_data'}, 'AAPL')
        assert chart == 'no data for chart for today'

    def test_chart_with_data(self):
        data = {'c':[1,2,3],
                't': [1607505000, 1607508600, 1607509800],
                'o':[1,2,3],
                'h':[2,3,4],
                'l':[1,1,1]}
        chart = createChart(data, 'AAPL')
        assert chart is not None

    def test_unixTimeConvertor(self):
        time = unixTimeConverter(1)
        assert time[0] is not None
        assert time[1] is not None

    @mock.patch('app.utils.todays_date')
    def test_unixTimeConvertor_weekday(self, mock_todays_date):
        mock_todays_date.return_value = datetime.datetime(2020, 12, 15, 4, 9, 34, 189783)
        time = unixTimeConverter(1)
        assert time[0] == '1608005374'
        assert time[1] == '1607918974'
