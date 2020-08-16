from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
app_name = 'mytransactions'



urlpatterns = [
          path('Buy',views.transactions,name='buy'),
          path('', views.my_stocks, name='my_stocks'),


    ]
