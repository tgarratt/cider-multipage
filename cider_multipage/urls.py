"""cider_multipage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from home.views import home
from contact_us.views import contact_us
from cart.views import cart_detail, cart_add, cart_remove
from sign_in.views import sign_in, sign_out
from products.views import products, get_add_product_form, productpk_delete, productpk_edit
from checkout.views import checkout
from admin_review.views import admin_review, infopk_delete
from django.contrib.auth import views as auth_views

app_name = "cider_multipage"

urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', home, name='home'),
    path(r'contact_us', contact_us, name='contact_us'),
    path(r'cart_detail', cart_detail, name='cart_detail'),
    path(r'add/<int:product_id>', cart_add, name='cart_add'),
    path(r'remove/<int:product_id>', cart_remove, name='cart_remove'),
    path(r'sign_in', sign_in, name='sign_in'),
    path(r'sign_out', sign_out, name='sign_out'),
    path(r'products', products, name='products'),
    path(r'get_add_product_form', get_add_product_form, name='get_add_product_form'),
    path(r'productpk_delete/<int:pk>', productpk_delete, name='productpk_delete'),
    path(r'productpk_edit/<int:pk>', productpk_edit, name='productpk_edit'),
    path(r'checkout', checkout, name='payment'),
    path(r'admin_review', admin_review, name='admin_review'),
    path(r'infopk_delete/<int:pk>', infopk_delete, name='infopk_delete'),
]
