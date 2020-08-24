from django.contrib.auth import views as auth_views
from . import views
from django.urls import path

app_name = 'mytransactions'
#
#
#
urlpatterns = [
    path("buy", views.buy_transactions, name='buy'),
    path("buy_unit_cost", views.get_buy_cost_and_unit, name="buy_unit_cost"),
    # path('sell', views.selltransactions, name='sell'),
    # path('base',views.base1,name='base'),
    path('', views.base, name='base'),
]
