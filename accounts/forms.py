from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# class customempregistrationform(UserCreationForm):
#
#     class Meta:
#         model=Employee
#         fields=['employeeId','password1','password2']

class userregistrationform(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

