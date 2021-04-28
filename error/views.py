from django.shortcuts import render
from cart.cart import Cart


def error_404(request, exception):
    # returns Errorpage

    cart = Cart(request)
         
    n = 0
    for item in cart:
        q = item['quantity']
        n = n + q
    print(n)
    print("^ cart items")

    return render(request, "../templates/error404.html",
        {'n': n})


def error_500(request):
    # returns Errorpage

    cart = Cart(request)
         
    n = 0
    for item in cart:
        q = item['quantity']
        n = n + q
    print(n)

    return render(request, "../templates/error500.html",
        {'n': n})