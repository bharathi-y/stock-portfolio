from django.shortcuts import render,redirect
from requests import Response

from .models import StockSummary, AllStocks
from .forms import AllStockForm, BuyForm,SellForm
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def base(request):
    return render(request, 'transtemp/base.html', context={})


def buy_transactions(request):
    all_stock_form = AllStockForm()
    buy_stock_form = BuyForm()

    if request.method == 'POST':
        stock = request.POST.get("stock_name")
        currency = request.POST.get("currency")
        unit = int(request.POST.get("stock_buy_units"))
        cost = float(request.POST.get("stock_price_per_unit"))
        fee = float(request.POST.get("fee"))
        buy_stock_form = BuyForm(request.POST)
        all_stock_form = AllStockForm(request.POST)
        if buy_stock_form.is_valid():
            buy_stock = buy_stock_form.save(commit=False)
            all_obj, created = AllStocks.objects.get_or_create(stock_name=stock, currency=currency)
            is_stock_exists = StockSummary.objects.filter(stock_name=all_obj).exists()

            if not is_stock_exists and created:
                stock_summary = StockSummary(
                    stock_name=all_obj, currency=currency, total_stock_holding_units=unit,
                    total_stock_holding_cost=unit * cost + fee
                )
                stock_summary.save()
                buy_stock.stock_name = all_obj
                buy_stock.currency = currency
                buy_stock.stock_total_cost = unit * cost + fee
            else:
                stock_summary = StockSummary.objects.get(stock_name=all_obj)
                stock_summary.total_stock_holding_units += unit
                stock_summary.total_stock_holding_cost += unit * cost + fee
                stock_summary.save()
                # insert records into buy table
                buy_stock.stock_name = all_obj
                buy_stock.currency = currency
                buy_stock.stock_total_cost = unit * cost + fee
                # all_stock_form.cleaned_data()

            buy_stock.save()

    return render(request, 'transtemp/buy.html', context={'buystocks': buy_stock_form, 'stockform': all_stock_form})


def sell_transactions(request):
    all_stock_form = AllStockForm()
    sell_stock_form = SellForm()
    if request.method == 'POST':
        stock = request.POST.get("stock_name")
        currency = request.POST.get("currency")
        unit = int(request.POST.get("stock_buy_units"))
        cost = float(request.POST.get("stock_price_per_unit"))
        fee = float(request.POST.get("fee"))
        try :
            all_obj=AllStocks.objects.get(stock_name=stock, currency=currency).exists()
            stock_summary = StockSummary.objects.get(stock_name=all_obj)
            if sell_stock_form.is_valid():
                sell_stock = sell_stock_form.save(commit=False)
                sell_stock.stock_name = all_obj
                sell_stock.currency = currency
                # sell_stock.stock_total_cost = unit * cost + fee
                # stock_summary.total_stock_holding_units -= unit
                stock_summary.total_stock_holding_cost -= unit * cost + fee
                stock_summary.total_stock_holding_unit -= unit * cost + fee
                stock_summary.save()
        except AllStocks.ObjectDoesNotExist:
            return Response(AllStocks.objects.none())
    return render(request, 'transtemp/buy.html', context={'sellstocks': sell_stock_form, 'stockform': all_stock_form})