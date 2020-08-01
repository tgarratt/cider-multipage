from django.shortcuts import render
from cart.models import CheckoutUserInfo
from cart.cart import Cart


def admin_review(request):
    # returns homepage

    all_checkoutuserinfo = CheckoutUserInfo.objects.all()

    return render(request, "../templates/admin_review.html",
        {"all_checkoutuserinfo": all_checkoutuserinfo})