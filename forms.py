from django import forms

class FixData(forms.Form):

    message_type = forms.CharField(label='message type', max_length=50)
    stock_symbol = forms.CharField(label='stock symbol', max_length=20)
    quantity = forms.IntegerField(label='quantity of stock')
    price = forms.DecimalField(label='price of stock', required=True)
    side = forms.CharField(max_length=50)
    order_type = forms.CharField(max_length=50)



    """
    {'message_type': ['New Order Single'],
     'stock_symbol': ['AAPL'],
     'quantity': ['1'],
     'price': ['123'],
     'side': ['Buy'],
     'order_type': ['Market']}
    """