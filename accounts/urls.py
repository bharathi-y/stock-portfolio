from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
app_name = 'accounts'
app_name='transactions'


urlpatterns = [
         # path('employeeregister/',views.employeeregistrationpage,name="employeeregistrationpage"),
         path('userregister/',views.userregistrationpage,name="userregistrationpage"),
         path('userlogin/',auth_views.LoginView.as_view(template_name='accounts/userloginpage.html'),name="userloginpage"),
         path('userlogout/',auth_views.LogoutView.as_view(template_name='accounts/userlogoutpage.html'),name="userlogoutpage"),

         # path('emplogout/',auth_views.LogoutView.as_view(template_name='accounts/emplogoutpage.html'),name="emplogoutpage"),
    ]
