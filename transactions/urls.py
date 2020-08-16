from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
app_name = 'transactions'



urlpatterns = [
         # path('employeeregister/',views.employeeregistrationpage,name="employeeregistrationpage"),
         # path('',views.home,name='home'),
         # path('Buy',views.transactions,name='buy'),
         # path('', views.my_stocks, name='my_stocks'),
         # path('test', views.last_update_date, name='test'),
         # path('emplogout/',auth_views.LogoutView.as_view(template_name='accounts/emplogoutpage.html'),name="emplogoutpage"),
    ]
