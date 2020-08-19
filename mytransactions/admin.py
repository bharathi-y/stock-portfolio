from django.contrib import admin
from .models import AllStock,MyTransactions

# Register your models here.
@admin.register(AllStock)
class AllStockAdmin(admin.ModelAdmin):
    list_display = ['stock','date_of_transaction','type','currency','transaction_unit','transaction_price_per_unit','fee']
    list_per_page = 30

@admin.register(MyTransactions)
class MyTransactionsAdmin(admin.ModelAdmin):
    list_display=['stock_id','stock_previous_date','stock_previous_unit','stock_cumulative_unit','stock_transacated_value'
           ,'stock_previous_cost','cost_of_transaction','cost_of_transaction_perunit','stock_cumulative_cost'
           , 'gain_loss_from_sale','yield_of_transactions','cash_flow']
    list_per_page=30
