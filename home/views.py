from django.shortcuts import render, redirect, reverse
from products.models import add_product
from cart.forms import CartAddProductForm

def home(request):
    # returns homepage

    featured = add_product.objects.filter(featured=True)[:3]

    cart_product_form = CartAddProductForm()

    return render(request, "../templates/home.html", {
        "featured": featured,
        "cart_product_form": cart_product_form})
