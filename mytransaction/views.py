from django.shortcuts import render,HttpResponse
from .models import SellStockTransactiontable, BuyStockTransactiontable, StockSummary, AllStocks
from .forms import AllStockForm, BuyForm, SellForm


# Create your views here.
def base(request):
    return render(request, 'transtemp/base.html', context={})


#
#
def buytransactions(request,pk=None):
    if request.method == 'POST':
        stock = request.POST.get("stock_name")
        currency = request.POST.get("currency")
        unit = request.POST.get("stock_buy_units")
        cost = request.POST.get("stock_price_per_unit")
        fee = request.POST.get("fee")
        allobj, created = AllStocks.objects.get_or_create(stock_name=stock)
        print("obj1")
        if not StockSummary.objects.filter(pk=pk,stock_name=allobj).exists():
            ssobj = StockSummary.objects.get(stock_name=allobj)
            ssobj.stock_name = stock
            ssobj.currency=currency
            ssobj.total_stock_holding_units = ssobj.total_stock_holding_units + unit
            ssobj.total_stock_holding_cost = ssobj.total_stock_holding_cost + unit*cost+fee
            print("inside if not")




        else:
            ssobj = StockSummary.objects.get(stock_name=allobj)
            ssobj.total_stock_holding_units = ssobj.total_stock_holding_units + unit
            ssobj.total_stock_holding_cost = ssobj.total_stock_holding_cost + unit * cost + fee
            print("inside if not")




        print(ssobj.stock_name)


        stockform = AllStockForm(request.POST)
        print("post",stockform)
        buystocks = BuyForm(request.POST)
        print("bpost")
        if created:
            if  buystocks.is_valid():
                print("insideif")
                buyobjc = buystocks.save(commit=False)
                allstockobjc = stockform.save(commit=False)
                buyobjc.stock_name = allobj
                buyobjc.currency = currency
                allobj.currency = currency
                buyobjc.stock_total_cost = buyobjc.stock_price_per_unit * buyobjc.stock_buy_units + buyobjc.fee
                ssobj.total_stock_holding_units=ssobj.total_stock_holding_units+buyobjc.stock_buy_units
                ssobj.total_stock_holding_cost=ssobj.total_stock_holding_cost+buyobjc.stock_total_cost
                buyobjc.save()
                allstockobjc.save()
        else:
            if buystocks.is_valid() :
                print("insideelseif")

                buyobj = buystocks.save(commit=False)
                buyobj.stock_name = allobj
                buyobj.currency = currency
                buyobj.stock_total_cost = buyobj.stock_price_per_unit * buyobj.stock_buy_units + buyobj.fee
                ssobj.total_stock_holding_units = ssobj.total_stock_holding_units + buyobj.stock_buy_units
                ssobj.total_stock_holding_cost = ssobj.total_stock_holding_cost + buyobj.stock_total_cost
                buyobj.save()



    else:
        buystocks = BuyForm()
        stockform = AllStockForm()
    return render(request, 'transtemp/buy.html', context={'buystocks': buystocks, 'stockform': stockform})
