#
# # Create your views here.
# # from django.contrib.auth.decorators import login_required
# from django.shortcuts import render,redirect,HttpResponse
# from django.contrib import messages
# from .forms import BuyForm
# from .models import All_Stock
# from django.core.exceptions import ObjectDoesNotExist
#
#
#
# def home(request) :
#     return render(request,'transtemp/base.html',context={})
#
#
# def transactions(request) :
#     if request.method == 'POST':
#             buystocks = BuyForm(request.POST)
#             if buystocks.is_valid():
#                 buystocks.save()
#                 return redirect('transactions_urls:my_stocks')
#
#     else:
#         buystocks = BuyForm()
#         return render(request,'transtemp/buy.html',context={'buystocks': buystocks })
#
#
#
# def my_stocks(request):
#     mystocks = All_Stock.objects.all()
#     return render(request, 'transtemp/mystocks.html', context={'mystocks': mystocks,})
# #
# # def last_update_date(request):
# #     filt_stocks = AllStock.objects.filter( )
# #     return render(request,'transtemp/test.html',context={"filt_stocks": filt_stocks})