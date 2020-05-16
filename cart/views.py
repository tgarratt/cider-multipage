from django.shortcuts import render


def cart(request):
    # returns homepage
    
    return render(request, "../templates/cart.html")
