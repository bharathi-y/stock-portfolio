from django.contrib import admin

# Register your models here.
from .models  import AllStock
from django.contrib import admin
# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ['employee', 'employeeId', 'email_id']
#     list_filter = ['employeeId']
#     list_per_page = 10


@admin.register(AllStock)
class AllStockAdmin(admin.ModelAdmin):
    list_display = ['user','Date','Stock']

    list_per_page = 10


# Register your models here.
