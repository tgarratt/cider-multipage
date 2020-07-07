from django.contrib import admin
from .models import OrderProduct, CheckoutUserInfo

admin.site.register(OrderProduct)

admin.site.register(CheckoutUserInfo)