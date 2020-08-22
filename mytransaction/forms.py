from django import forms
from .models import SellStockTransactiontable, BuyStockTransactiontable,AllStocks


class DateInput(forms.DateInput):
    input_type = 'date'

class StockForm(forms.ModelForm):
    class Meta:
        model=AllStocks
        fields=("stock_name","currency")

class BuyForm(forms.ModelForm):
    class Meta:
        model = BuyStockTransactiontable
        widgets = {'stock_buy_transacted_date': DateInput()}
        fields = ( "stock_buy_transacted_date",
                  "stock_buy_units", "stock_price_per_unit",
                  "fee")


class SellForm(forms.ModelForm):
    class Meta:
        model = SellStockTransactiontable
        widgets = {'stock_sell_transacted_date': DateInput()}
        fields = ("stock_sell_transacted_date", "stock_sell_units"
                  , "stock_price_per_unit", "fee")


from django.contrib import admin

# Register your models here.
