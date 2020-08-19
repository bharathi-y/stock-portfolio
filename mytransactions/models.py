from django.db import models

# Create your models here.
from django.db import models
# from django.contrib.auth.models import User


class AllStock(models.Model):
    buy_choice = (("Sell", "Sell"),
                  ("Buy", "Buy"))

    curr_choice = (("USD", "United States Dollar"),
                   ("HKD", "Hong Kong dollar"))
    stock = models.CharField(max_length=120, help_text='please select the stock')
    date_of_transaction = models.DateField()
    type = models.CharField(max_length=8,choices=buy_choice,null=True,blank=True,help_text="Bought or sell")
    currency = models.CharField(max_length=3,choices=curr_choice,help_text="choice the currenct ")
    transaction_unit = models.IntegerField(help_text="number of stocks transacted")
    transaction_price_per_unit = models.FloatField(help_text="price per unit")
    fee = models.FloatField(help_text="Fee Payed ")

    def __str__(self):
        return "(0) - {1}".format(self.stock,self.date_of_transaction,self.type,self.currency,self.transaction_unit,self.transaction_price_per_unit,self.fee)




class MyTransactions(models.Model):
    stock_id=models.OneToOneField(AllStock, help_text='User of the POST', on_delete=models.CASCADE)
    stock_previous_date = models.DateField()
    stock_previous_unit=models.IntegerField()
    stock_cumulative_unit= models.IntegerField(help_text="number of stocks transacted")
    stock_transacated_value= models.IntegerField(help_text="number of stocks transacted")
    stock_previous_cost=models.FloatField()
    cost_of_transaction=models.IntegerField()
    cost_of_transaction_perunit=models.IntegerField()
    stock_cumulative_cost=models.IntegerField()
    gain_loss_from_sale=models.IntegerField()
    yield_of_transactions=models.IntegerField()
    cash_flow=models.IntegerField()
    def __str__(self):
        return "(0) - {1}".format(self.stock_id,self.stock_previous_date,self.stock_previous_unit,self.stock_cumulative_unit
                                  ,self.stock_transacated_value,self.stock_previous_cost,self.cost_of_transaction,self.cost_of_transaction_perunit,self.stock_cumulative_cost
                                   ,self.gain_loss_from_sale,self.yield_of_transactions,self.cash_flow)
