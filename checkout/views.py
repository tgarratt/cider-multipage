from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from decimal import Decimal
from cart.cart import Cart
from .forms import payment_form
from cart.cart import Cart
from django.conf import settings
from cart.forms import CheckoutUserInfoForm
import json
import stripe


stripe.api_key = settings.STRIPE_SECRET


def checkout(request):

    #amount_total = request.session.get('cart_total_cost') 
    #print(amount_total)

    if request.method == "POST":
        print(request.POST)
        
        checkout_user_info = CheckoutUserInfoForm(request.POST, request.FILES)
        
        if checkout_user_info.is_valid():
            print("validinfo")
            
    else:
        checkout_user_info = CheckoutUserInfoForm()

    payment_amount = (100)

    if request.method == "POST":
        payment = payment_form(request.POST)

        if payment.is_valid():
            price = payment_amount
            try:
                customer = stripe.Charge.create(
                    amount=int(price * 100),
                    currency="GBP",
                    card=payment.cleaned_data['stripe_id'],
                )

                if customer.paid:
                    
                    checkout_user_info.save()
                    messages.success(request, "You have successfully paid!")
                    return redirect(reverse("home"))

                else:
                    messages.error(request, "Unable to take payment!")

            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

        else:
            print(payment.errors)
            messages.error(
                request, "We were unable to take payment with that card!")

    else:
        payment = payment_form()
    
    
    return render(
        request, "../templates/checkout.html", {
            'payment': payment,
            'publishable': settings.STRIPE_PUBLISHABLE,
            'payment_amount': payment_amount,
            'checkout_user_info': checkout_user_info})