from django.contrib import admin
from .models import Order, Cart


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'total_price', 'created', 'condition')
    list_display_links = ('id', 'name')
    search_fields = ('id',)


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'product', 'quantity')
    list_display_links = ('id', 'order')
    search_fields = ('id',)


admin.site.register(Order, OrderAdmin)
admin.site.register(Cart, CartAdmin)