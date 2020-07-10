from django.db import models
from django.utils import timezone
from products.models import add_product

# Create your models here.

class OrderProduct(models.Model):
    product = models.OneToOneField(add_product, on_delete=models.SET_NULL, null=True)
    ordered = models.BooleanField(default=False)
    when = models.DateTimeField(null=True)


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    items = models.ManyToManyField(OrderProduct)
    date_ordered = models.DateTimeField(auto_now=True)

class CheckoutUserInfo(models.Model):
    user_email = models.EmailField(verbose_name='E-mail', max_length=30)
    user_name = models.CharField(verbose_name='Full name', max_length=60)
    user_country = models.CharField(verbose_name='Country', max_length=60)
    user_city = models.CharField(verbose_name='City', max_length=60)
    user_line1 = models.CharField(verbose_name='Address line 1', max_length=60)
    user_line2 = models.CharField(verbose_name='Address line 2', max_length=60)
    user_postcode = models.CharField(verbose_name='Postcode', max_length=60)
    user_countystate = models.CharField(verbose_name='County/State', max_length=60)
    user_price_total = models.FloatField(default=0)
    order_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)

    def __str__(self):
        return self.user_email + " / " + self.user_name