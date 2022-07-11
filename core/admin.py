from django.contrib import admin
from .models import Order, Customer


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('reference', 'amount', 'customer')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'city', 'zip_code')
