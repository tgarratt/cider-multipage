from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from cart.forms import CartAddProductForm
from .models import add_product
from .forms import add_product_form
from cart.cart import Cart


def products(request):
    # returns homepage

    cart = Cart(request)

    n = 0
    q = 0

    for item in cart:
        q = item['quantity']
        n = n + q

    print(n)

    if q == 20:
        messages.info(
                request, "Maximum single item quantity of 20 reached!")

    all_products = add_product.objects.all()
    cart_product_form = CartAddProductForm()



    return render(request, "../templates/products.html", 
    {"all_products": all_products,
    "cart_product_form": cart_product_form,
    "n": n})


def get_add_product_form(request):
    # add product form

    cart = Cart(request)
         
    n = 0
    for item in cart:
        q = item['quantity']
        n = n + q
    print(n)

    if request.method == "POST":
        print(request.POST)
        product_form = add_product_form(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect(reverse('products'))
    else:
        product_form = add_product_form()

    return render(request, "../templates/add_product.html", {"product_form": product_form,
        'n': n})

def productpk_delete(request, pk=None):
    # deletes selected product

    delete_product = get_object_or_404(add_product, pk=pk)
    delete_product.delete()

    return redirect(reverse('products'))

def productpk_edit(request, pk):
    # deletes selected product

    cart = Cart(request)
         
    n = 0
    for item in cart:
        q = item['quantity']
        n = n + q
    print(n)


    edit_product = get_object_or_404(add_product, pk=pk)

    if request.method == "POST":

        edit_info_product = add_product_form(
            request.POST, request.FILES, instance=edit_product)
        if edit_info_product.is_valid():
            edit_product = edit_product.save()
            edit_info_product.save()
            return redirect(reverse('products'))

    else:
        edit_info_product = add_product_form(instance=edit_product)

    return render(request, "../templates/product_edit.html", {
        "edit_info": edit_info_product,
        "n": n})
