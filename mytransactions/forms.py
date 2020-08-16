from django import forms
from .models import AllStock

class DateInput(forms.DateInput):
     input_type='date'

class BuyForm(forms.ModelForm):
    class Meta:
        model = AllStock
        widgets={'date_of_transaction':DateInput()}
        fields = ('stock','date_of_transaction','transaction_unit','currency','transaction_price_per_unit','type','fee')


