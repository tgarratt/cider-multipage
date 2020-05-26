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
from django.urls import path
from home.views import home
from products.views import products
from contact_us.views import contact_us
from our_story.views import our_story
from cart.views import cart
from sign_in.views import sign_in, sign_out
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path(r'', home, name='home'),
    path(r'products', products, name='products'),
    path(r'contact_us', contact_us, name='contact_us'),
    path(r'our_story', our_story, name='our_story'),
    path(r'cart', cart, name='cart'),
    path(r'sign_in', sign_in, name='sign_in'),
    path(r'sign_out', sign_out, name='sign_out'),
]
