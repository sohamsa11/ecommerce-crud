# Register your models here.
from django.contrib import admin
from .models import Product, Customer, Order

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'stock_quantity', 'description')
    search_fields = ['name']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_number', 'address')
    search_fields = ['name', 'email']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'product', 'quantity', 'order_date', 'status')
    search_fields = ['customer__name', 'product__name']
