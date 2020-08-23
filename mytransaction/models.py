from django.db import models
import datetime

class AllStocks(models.Model):
    curr_choice = (("SGD", "Singapore dollar"),
                   ("HKD", "Hong Kong dollar"),
                   ("USD", "United States Dollar"),
                   ("INR", "Indian Rupee"))
    stock_name=models.CharField(max_length=200,unique=True)
    currency=models.CharField(max_length=120, choices=curr_choice, help_text="choice the currenct ")
    def __str__(self):
        return "(0) – {1}".format(self.stock_name, self.currency)

# Create your models here.
class StockSummary(models.Model):
    currency = models.CharField(max_length=200)
    stock_name = models.OneToOneField(AllStocks, on_delete=models.CASCADE)
    total_stock_holding_units = models.IntegerField(default=0)
    total_stock_holding_cost = models.FloatField(default=0)
    unrealized_gain_loss = models.FloatField(default=0)
    unrealized_gain_loss_percentage = models.FloatField(default=0)
    realized_gain_loss = models.FloatField(default=0)
    total_gain_loss = models.FloatField(default=0)
    last_transacted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "(0) – {1}".format(self.currency, self.stock_name, self.total_stock_holding_units,
                                  self.total_stock_holding_cost
                                  , self.unrealized_gain_loss, self.unrealized_gain_loss_percentage,
                                  self.realized_gain_loss
                                  , self.total_gain_loss, self.last_transacted_date)


class BuyStock(models.Model):
    stock_buy_transacted_date = models.DateField()
    currency = models.CharField(max_length=200)
    stock_name = models.ForeignKey(AllStocks,help_text='User of the POST' , on_delete=models.CASCADE)
    stock_buy_units = models.IntegerField(help_text="number of stocks transacted")
    stock_price_per_unit = models.FloatField(help_text="price per unit")
    fee = models.FloatField(help_text="Fee Payed ")
    stock_total_cost = models.FloatField(default=0)
    last_transacted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "(0) – {1}".format(self.stock_buy_transacted_date, self.currency, self.stock_name,
                                  self.stock_buy_units, self.stock_price_per_unit,
                                  self.fee, self.stock_total_cost, self.last_transacted_date)


class SellStock(models.Model):
    stock_sell_transacted_date = models.DateField()
    currency = models.CharField(max_length=200)
    stock_name = models.ForeignKey(AllStocks,help_text='User of the POST' , on_delete=models.CASCADE)
    stock_sell_units = models.IntegerField(help_text="number of stocks transacted")
    stock_price_per_unit = models.FloatField(help_text="price per unit")
    fee = models.FloatField(help_text="Fee Payed ")
    stock_total_cost = models.FloatField(default=0)
    stock_transaction_cost = models.FloatField(default=0)
    stock_transaction_cost_per_unit = models.IntegerField(default=0)
    gain_loss_from_sell = models.FloatField(default=0)
    yield_of_transaction = models.FloatField(default=0)
    last_transacted_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "(0) – {1}".format(self.stock_sell_transacted_date, self.currency, self.stock_name, self.stock_sell_units
                                  , self.stock_price_per_unit, self.fee, self.stock_total_cost
                                  , self.stock_transaction_cost, self.stock_transaction_cost_per_unit
                                  , self.gain_loss_from_sell
                                  , self.yield_of_transaction
                                  , self.last_transacted_date)


# Create your models here.
