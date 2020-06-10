from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import OrderProduct, Order
from products.models import add_product

def cart(request):
    # returns homepage
    get_cart_items = OrderProduct.objects.all()
    return render(request, "../templates/cart.html", {"get_cart_items": get_cart_items})


def add_to_cart (request, pk=None):
    # adds product to the cart
    product = add_product.objects.filter(pk=pk).first()

    order_product, status = OrderProduct.objects.get_or_create(product=product)
    print(OrderProduct.product)

    

    messages.success(request, "Item added to cart!")

    return redirect(reverse('cart'))
