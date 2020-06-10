from django.db import models
from products.models import add_bottle

# Create your models here.

class OrderProduct(models.Model):
    product = models.OneToOneField(add_bottle, on_delete=models.SET_NULL, null=True)
    ordered = models.BooleanField(default=False)
    when = models.DateTimeField(null=True)


class Order(models.Model):
    ref_code = models.CharField(max_length=15)
    items = models.ManyToManyField(OrderProduct)
    date_ordered = models.DateTimeField(auto_now=True)