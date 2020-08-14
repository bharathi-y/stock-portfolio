from django.db import models
from django.contrib.auth.models import User


class AllStock(models.Model):
    buy_choice = (("Div", "Div"),
                  ("Sell", "Sell"),
                  ("Buy", "Buy"),
                  ("Split", "Split"),
                  ("CapReduct", "CapReduct"))

    curr_choice = (("USD", "United States Dollar"),
                   ("HKD", "Hong Kong dollar"))
    user= models.ForeignKey(User,help_text= 'employee raising  the request',on_delete=models.CASCADE)
    Date = models.DateTimeField(auto_now_add=True)
    Type = models.CharField(max_length=10,choices=buy_choice,null=True,blank=True)
    Stock = models.CharField(max_length=120, help_text='please select the stock')
    Currency = models.CharField(max_length=3,choices=curr_choice)
    TransactionUnit = models.IntegerField()
    TransactionPrice = models.FloatField(max_length=100)

    def __str__(self):
        return "(0) - {1}".format(self.user,self.Date,self.Type,self.Stock,self.Currency,self.TransactionUnit,self.TransactionPrice)

