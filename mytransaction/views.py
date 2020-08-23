from django.shortcuts import render, HttpResponse
from .models import SellStock, BuyStock, StockSummary, AllStocks
from .forms import AllStockForm, BuyForm, SellForm


# Create your views here.
def base(request):
    return render(request, 'transtemp/base.html', context={})


#
#
def buytransactions(request, pk=None):
    all_stock_form = AllStockForm()
    buy_stock_form = BuyForm()
    if request.method == 'POST':
        stock = request.POST.get("stock_name")
        currency = request.POST.get("currency")
        unit = int(request.POST.get("stock_buy_units"))
        cost = float(request.POST.get("stock_price_per_unit"))
        fee = float(request.POST.get("fee"))
        all_stock_form = AllStockForm(request.POST)
        buy_stock_form = BuyForm(request.POST)
        if buy_stock_form.is_valid():
            buy_stock = buy_stock_form.save(commit=False)
            all_obj, created = AllStocks.objects.get_or_create(stock_name=stock, currency=currency)
            is_stock_exists = StockSummary.objects.filter(stock_name=all_obj).exists()
            if not is_stock_exists:
                if all_stock_form.is_valid():
                    stock_summary = StockSummary(
                        stock_name=all_obj, currency=currency, total_stock_holding_units=unit,
                        total_stock_holding_cost=unit * cost + fee
                    )
                    stock_summary.save()
                    buy_stock.stock_name = all_obj
                    buy_stock.currency = currency
                    buy_stock.stock_total_cost = unit * cost + fee
                    buy_stock.save()
                    all_stock_form.save()
            elif all_stock_form.is_valid():
                stock_summary = StockSummary.objects.get(stock_name=all_obj)
                stock_summary.total_stock_holding_units += unit
                stock_summary.total_stock_holding_cost += unit * cost + fee
                stock_summary.save()
                buy_stock.stock_name = all_obj
                buy_stock.currency = currency
                buy_stock.stock_total_cost = unit * cost + fee
                buy_stock.save()
    return render(request, 'transtemp/buy.html', context={'buystocks': buy_stock_form, 'stockform': all_stock_form})
