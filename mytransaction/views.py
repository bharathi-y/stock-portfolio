from django.shortcuts import render
from mytransaction.models import StockSummary, AllStocks
from mytransaction.forms import AllStockForm, BuyForm
from django.http import JsonResponse


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
                buy_stock.stock_name = all_obj
                buy_stock.currency = currency
                buy_stock.stock_total_cost = unit * cost + fee
            else:
                stock_summary = StockSummary.objects.get(stock_name=all_obj)
                stock_summary.total_stock_holding_units += unit
                stock_summary.total_stock_holding_cost += unit * cost + fee
                # insert records into buy table
                buy_stock.stock_name = all_obj
                buy_stock.currency = currency
                buy_stock.stock_total_cost = unit * cost + fee
                all_stock_form.cleaned_data
            stock_summary.save()
            buy_stock.save()
    return render(request, 'transtemp/buy.html', context={'buystocks': buy_stock_form, 'stockform': all_stock_form})


def get_buy_cost_and_unit(request):
    if request.method == 'GET':
        print(f"request  {request.GET}")
        stock = request.GET.get("stock_name")
        currency = request.GET.get("currency")
        is_stock_exists = AllStocks.objects.filter(stock_name=stock, currency=currency).exists()
        resp = {"unit": 0, "cost": 0.0}
        if is_stock_exists:
            stock = AllStocks.objects.get(stock_name=stock, currency=currency)
            stock_summary = StockSummary.objects.get(stock_name=stock)
            print(stock_summary)
            resp = {"unit": stock_summary.total_stock_holding_units, "cost": stock_summary.total_stock_holding_cost}
        return JsonResponse(resp)
