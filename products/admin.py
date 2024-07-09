# products/admin.py
from django.contrib import admin
from .models import Category, Product, Review, Wishlist


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'seller', 'date_added')
    search_fields = ('name', 'description')
    list_filter = ('category', 'date_added')


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('product', 'user', 'rating', 'date_added')
    search_fields = ('comment',)
    list_filter = ('rating', 'date_added')


class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user', 'date_added')
    search_fields = ('user__username',)


admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Wishlist, WishlistAdmin)
