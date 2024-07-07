# cart/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Cart, CartItem
from products.models import Product

@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    cart_item.quantity = quantity
    cart_item.save()
    return redirect('view_cart')

@login_required
def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    return render(request, 'cart/view_cart.html', {'cart': cart})

@login_required
def update_cart(request):
    cart = get_object_or_404(Cart, user=request.user)
    for item in cart.items.all():
        quantity = request.POST.get(f'quantity_{item.pk}')
        if quantity:
            item.quantity = int(quantity)
            item.save()
    return redirect('view_cart')

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id)
    item.delete()
    return redirect('view_cart')

@login_required
def checkout(request):
    cart = get_object_or_404(Cart, user=request.user)
    # Implement checkout logic here (e.g., payment processing, order confirmation)
    return render(request, 'cart/checkout.html', {'cart': cart})
