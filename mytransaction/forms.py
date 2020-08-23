from django import forms
from .models import SellStock, BuyStock,AllStocks


class DateInput(forms.DateInput):
    input_type = 'date'

class AllStockForm(forms.ModelForm):
    class Meta:
        model=AllStocks
        fields=('stock_name','currency')

class BuyForm(forms.ModelForm):
    class Meta:
        model = BuyStock
        widgets = {'stock_buy_transacted_date': DateInput()}
        fields = ( 'stock_buy_transacted_date',
                  'stock_buy_units', 'stock_price_per_unit',
                  'fee')


class SellForm(forms.ModelForm):
    class Meta:
        model = SellStock
        widgets = {'stock_sell_transacted_date': DateInput()}
        fields = ("stock_sell_transacted_date", "stock_sell_units"
                  , "stock_price_per_unit", "fee")


from django.contrib import admin

# Register your models here.
