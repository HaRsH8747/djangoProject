# cart/admin.py
from django.contrib import admin
from .models import Cart, CartItem


class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)
    search_fields = ('user__username',)
    list_filter = ('user',)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    search_fields = ('cart__user__username', 'product__name')
    list_filter = ('cart', 'product')


admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
