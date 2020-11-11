from rest_framework import serializers
from app.models import StockData

# class StockDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = StockData
#         fields = ['id', 'stock_symbol', 'order_type', 'quantity',
#             'fix_message', 'created']
