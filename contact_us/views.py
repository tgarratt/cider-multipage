from django.shortcuts import render
from cart.cart import Cart


def contact_us(request):

    cart = Cart(request)
         
    n = 0
    for item in cart:
        q = item['quantity']
        n = n + q
    print(n)
    print("^ cart items")

    return render(request, "../templates/contact_us.html",
        {'n': n})
