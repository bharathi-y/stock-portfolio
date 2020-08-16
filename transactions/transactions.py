#
#
# from .models import AllStock
# from django.shortcuts import render,redirect,HttpResponse
# from django.core.exceptions import ObjectDoesNotExist
# from django.contrib import messages
# from datetime import date
# # class Transactions() :
# #     def __init__(self,Stock_Name,TransactionUnit,TransactionPrice,Fees,StockSplitRatio=1) :
# #         self.Stock_Name = Stock_Name
# #         self.TransactionUnit=TransactionUnit
# #         self.TransactioPrice=TransactionPrice
# #         self.Fees=Fees
# #         self.StockSplitRatio=StockSplitRatio
#
# def last_update_date(request):
#     try:
#         date = AllStock.objects.get(pk=id, Stock=request.Stock)
#     except ObjectDoesNotExist:
#         messages.error(request, 'Invalid user to access this post')
#         return redirect('/')
#     return render(request,"",context={"date":date})
