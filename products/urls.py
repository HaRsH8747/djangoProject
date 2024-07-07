# products/urls.py
from django.urls import path
from .views import product_list, product_detail, add_product, edit_product, delete_product, search_products, add_review, search_suggestions

urlpatterns = [
    path('', product_list, name='product_list'),
    path('<int:pk>/', product_detail, name='product_detail'),
    path('add/', add_product, name='add_product'),
    path('<int:pk>/edit/', edit_product, name='edit_product'),
    path('<int:pk>/delete/', delete_product, name='delete_product'),
    path('search_suggestions/', search_suggestions, name='search_suggestions'),
    path('search/', search_products, name='search_products'),
    path('<int:pk>/review/', add_review, name='add_review'),
]
