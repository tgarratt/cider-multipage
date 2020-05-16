from django.shortcuts import render, redirect, reverse
from products.models import add_bottle

def home(request):
    # returns homepage
    featured = add_bottle.objects.filter(featured=True)

    return render(request, "../templates/home.html", {"featured": featured})
