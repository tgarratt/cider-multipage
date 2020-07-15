from django.shortcuts import render,reverse, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.conf import settings
from products.models import add_product
from .cart import Cart
from .forms import CartAddProductForm


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(add_product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
 

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(add_product, id=product_id)
    cart.remove(product)
    return redirect('cart_detail')

def cart_detail(request):
    cart = Cart(request)
         
    url = request.path_info
    print(url)

    n = 0
    for item in cart:
        q = item['quantity']
        n = n + q
    print(n)

    i = 0
    for item in cart:
        i += 1
    print(i)

    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
            'update': True,})

    return render(request, 'cart.html', {'cart': cart,
        'n': n, 'i': i})