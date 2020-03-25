from django.shortcuts import render


def products(request):
    # returns homepage
    return render(request, "../templates/products.html")
