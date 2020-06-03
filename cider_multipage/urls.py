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
from cart.views import cart
from sign_in.views import sign_in, sign_out
from products.views import products, get_add_bottle_form, get_add_crate_form, get_add_keg_form, bottlepk_delete, cratepk_delete, kegpk_delete, bottlepk_edit, cratepk_edit, kegpk_edit
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', home, name='home'),
    path(r'contact_us', contact_us, name='contact_us'),
    path(r'cart', cart, name='cart'),
    path(r'sign_in', sign_in, name='sign_in'),
    path(r'sign_out', sign_out, name='sign_out'),
    path(r'products', products, name='products'),
    path(r'get_add_bottle_form', get_add_bottle_form, name='get_add_bottle_form'),
    path(r'get_add_crate_form', get_add_crate_form, name='get_add_crate_form'),
    path(r'get_add_keg_form', get_add_keg_form, name='get_add_keg_form'),
    path(r'bottlepk_delete/(?P<pk>\d+)', bottlepk_delete, name='bottlepk_delete'),
    path(r'bottlepk_edit/(?P<pk>\d+)', bottlepk_edit, name='bottlepk_edit'),
    path(r'cratepk_delete/(?P<pk>\d+)', cratepk_delete, name='cratepk_delete'),
    path(r'cratepk_edit/(?P<pk>\d+)', cratepk_edit, name='cratepk_edit'),
    path(r'kegpk_delete/(?P<pk>\d+)', kegpk_delete, name='kegpk_delete'),
    path(r'kegpk_edit/(?P<pk>\d+)', kegpk_edit, name='kegpk_edit'),
]
