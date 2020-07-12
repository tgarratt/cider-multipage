from django.shortcuts import render, redirect, reverse
from products.models import add_product
from cart.forms import CartAddProductForm
from cart.cart import Cart

def home(request):
    # returns homepage

    cart = Cart(request)
         
    n = 0
    for item in cart:
        q = item['quantity']
        n = n + q
    print(n)

    featured = add_product.objects.filter(featured=True)[:3]

    cart_product_form = CartAddProductForm()

    return render(request, "../templates/home.html", {
        "featured": featured,
        "cart_product_form": cart_product_form,
        "n": n
        })
