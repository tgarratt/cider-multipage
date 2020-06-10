from django.shortcuts import render, redirect, reverse
from products.models import add_product

def home(request):
    # returns homepage

    featured = add_product.objects.filter(featured=True)[:3]

    return render(request, "../templates/home.html", {"featured": featured})
