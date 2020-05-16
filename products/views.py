from django.shortcuts import render
from .models import add_bottle, add_crate, add_keg


def products(request):
    # returns homepage
    add_bottles = add_bottle.objects.all()
    add_crates = add_crate.objects.all()
    add_kegs = add_keg.objects.all()

    return render(request, "../templates/products.html", 
    {"add_bottles": add_bottles,
    "add_crates": add_crates,
    "add_kegs": add_kegs})
