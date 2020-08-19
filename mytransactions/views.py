# Create your views here.
# from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .forms import BuyForm
from itertools import chain
from .models import AllStock,MyTransactions
from django.core.exceptions import ObjectDoesNotExist


def base(request):
    return render(request, 'transtemp/base.html', context={})


def transactions(request,pk=None):

    if request.method == 'POST':

        obj=AllStock.objects.filter(stock=request.POST.get("stock")).order_by("-id").first()
        obj1=MyTransactions.objects.filter(stock_id=obj.id)

        print(obj.id,obj.stock,obj.date_of_transaction)
        buystocks = BuyForm(request.POST)
        if buystocks.is_valid():
            obj2=buystocks.save(commit=False)
            obj1.stock_previous_date=obj.date_of_transaction
            obj1.transaction_unit=obj.stock_previous_unit
            obj1.p


            obj2.save()

            return redirect('transactions_urls:my_stocks')

    else:
        buystocks = BuyForm()
        return render(request, 'transtemp/buysellstock.html', context={'buystocks': buystocks})


def my_stocks(request):

    object_list=MyTransactions.objects.all().select_related('stock')



    return render(request, 'transtemp/mystocks.html', context={'object_lits': object_list })


#
# def last_update_date(request):
#     filt_stocks = AllStock.objects.filter( )
#     return render(request,'transtemp/test.html',context={"filt_stocks": filt_stocks})


# Create your views here.
