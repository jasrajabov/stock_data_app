from django.db import models

# Create your models here.
class StockData(models.Model):
    stock_symbol = models.CharField(max_length=10)
    stock_price = models.DecimalField(max_digits=50, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    quantity =models.IntegerField()
