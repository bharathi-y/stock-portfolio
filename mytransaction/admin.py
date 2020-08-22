from django.contrib import admin
from .models import BuyStockTransactiontable, SellStockTransactiontable, StockSummary,AllStocks

@admin.register(AllStocks)
class AllStockAdmin(admin.ModelAdmin):
    list_display = ["stock_name","currency"]



 # Register your models here.
@admin.register(BuyStockTransactiontable)
class BuyStockTransactiontableAdmin(admin.ModelAdmin):
     list_display = ["stock_buy_transacted_date","stock_name","currency",
                     "stock_buy_units", "stock_price_per_unit",
                     "fee", "stock_total_cost", "last_transacted_date"]


@admin.register(SellStockTransactiontable)
class SellStockTransactiontableAdmin(admin.ModelAdmin):
     list_display = ["stock_sell_transacted_date", "stock_sell_units","stock_name","currency"
         , "stock_price_per_unit", "fee", "stock_total_cost"
         , "stock_transaction_cost", "stock_transaction_cost_per_unit", "gain_loss_from_sell"
         , "yield_of_transaction", "last_transacted_date"]
     list_per_page = 30


@admin.register(StockSummary)
class StockSummaryAdmin(admin.ModelAdmin):
     list_display = ["currency", "stock_name", "total_stock_holding_units",
                     "total_stock_holding_cost", "unrealized_gain_loss", "unrealized_gain_loss_percentage",
                     "realized_gain_loss",  "total_gain_loss", "last_transacted_date"]
     list_per_page = 30