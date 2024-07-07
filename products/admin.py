# products/admin.py
from django.contrib import admin
from .models import Category, Product, Review

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'seller', 'date_added')
    search_fields = ('name', 'description')
    list_filter = ('category', 'date_added')

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'date_added')
    search_fields = ('comment',)
    list_filter = ('rating', 'date_added')

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
