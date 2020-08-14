from django import forms
from .models import AllStock

class BuyForm(forms.ModelForm):
    class Meta:
        model = AllStock
        fields = ('Stock','TransactionUnit','Currency','TransactionPrice')


