from django.db import models

# Create your models here.
class StockData(models.Model):
    stock_symbol = models.CharField(max_length=10)
    order_type = models.CharField(max_length=40)
    quantity =models.IntegerField()
    fix_message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
