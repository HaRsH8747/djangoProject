# cart/urls.py
from django.urls import path
from .views import add_to_cart, view_cart, update_cart, remove_from_cart, checkout

urlpatterns = [
    path('add/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('view/', view_cart, name='view_cart'),
    path('update/', update_cart, name='update_cart'),
    path('remove/<int:item_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
]
