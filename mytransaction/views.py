from django.shortcuts import render
from .models import SellStockTransactiontable, BuyStockTransactiontable, StockSummary, AllStocks
from .forms import StockForm, BuyForm, SellForm


# Create your views here.
def base(request):
    return render(request, 'transtemp/base.html', context={})


#
#
def buytransactions(request):
    if request.method == 'POST':
        stock = request.POST.get("stock_name")
        obj1, created = AllStocks.objects.get_or_create(stock_name=stock)
        obj4 = StockSummary.objects.filter(stock_name=obj1).exists()
        if obj4:
            pass
        else:
            obj4.stock_name = obj1.stock_name
        buystocks = BuyForm(request.POST)
        stockform = StockForm(request.POST)
        if buystocks.is_valid() and stockform.is_valid():
            obj2 = buystocks.save(commit=False)
            obj3 = stockform.save(commit=False)
            obj2.stock_name = obj3.stockname
            obj2.currency = obj3.currency
            obj4.currency = obj3.currency
            obj1.currency = obj3.currency
            obj2.stock_total_cost = obj2.stock_price_per_unit * obj2.stock_buy_units + obj2.fee
            obj4.total_stock_holding_units = obj4.total_stock_holding_units.obj2.stock_buy_units
            obj4.total_stock_holding_cost = obj4.total_stock_holding_cost + obj2.stock_total_cost

    else:
        buystocks = BuyForm()
        stockform = StockForm()
        return render(request, 'transtemp/buy.html', context={'buystocks': buystocks, 'stockform': stockform})
