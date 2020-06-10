from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages
from .models import add_product
from .forms import add_product_form


def products(request):
    # returns homepage
    add_bottles = add_product.objects.filter(product_type="1")
    add_crates = add_product.objects.filter(product_type="2")
    add_kegs = add_product.objects.filter(product_type="3")

    return render(request, "../templates/products.html", 
    {"add_bottles": add_bottles,
    "add_crates": add_crates,
    "add_kegs": add_kegs})


def get_add_product_form(request):
    # add product form
    if request.method == "POST":
        print(request.POST)
        product_form = add_product_form(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return redirect(reverse('products'))
    else:
        product_form = add_product_form()

    return render(request, "../templates/add_bottle.html", {"product_form": product_form})

def productpk_delete(request, pk=None):
    # deletes selected product

    delete_product = get_object_or_404(add_product, pk=pk)
    delete_product.delete()

    return redirect(reverse('products'))

def productpk_edit(request, pk):
    # deletes selected product
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
        "edit_info": edit_info_product})
