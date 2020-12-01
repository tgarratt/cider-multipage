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

    return render(request, "../templates/error.html",
        {'n': n})
