
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect,HttpResponse
from django.contrib import messages
from .forms import BuyForm
from .models import AllStock


def home(request) :
    return render(request,'transtemp/base.html',context={})

@login_required(login_url='transactions_urls:my_stocks')
def transactions(request) :
    if request.method == 'POST':
            buystocks = BuyForm(request.POST)
            if buystocks.is_valid():
                f = buystocks.save(commit=False)
                f.user = request.user
                f.save()

                return redirect('transactions_urls:my_stocks')

    else:
        buystocks = BuyForm()
        return render(request,'transtemp/buy.html',context={'buystocks': buystocks })


@login_required(login_url='transactions_urls:my_stocks')
def my_stocks(request):
    mystocks = AllStock.objects.filter(user=request.user,)
    return render(request, 'transtemp/mystocks.html', context={'mystocks': mystocks,})