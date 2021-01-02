from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.admin.views.decorators import staff_member_required
from cart.models import CheckoutUserInfo
from cart.cart import Cart

@staff_member_required(login_url='sign_in')
def admin_review(request):
    # returns homepage

    all_checkoutuserinfo = CheckoutUserInfo.objects.all()

    num_orders = 0
    for item in all_checkoutuserinfo:
        num_orders += 1
    print(num_orders)

    return render(request, "../templates/admin_review.html",
        {"all_checkoutuserinfo": all_checkoutuserinfo, 'num_orders': num_orders})

def infopk_delete(request, pk=None):
    # deletes selected product

    delete_info = get_object_or_404(CheckoutUserInfo, pk=pk)
    delete_info.delete()

    return redirect(reverse('admin_review'))