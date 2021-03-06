from django.db import models
from cloudinary.models import CloudinaryField


class add_product(models.Model):

    PRODUCT_CHOICES = (
        ('1', 'Bottle'), ('2', 'Crate'), ('3', 'Keg'))
    product_type = models.CharField(
        max_length=50, choices=PRODUCT_CHOICES, default='')
    product_title = models.CharField(max_length=50, blank=False)
    product_price = models.DecimalField(max_digits=10, default=0, decimal_places=2)
    # product_img = models.ImageField(upload_to="static/img/product", blank=True, null=True)
    product_img = CloudinaryField('image', blank=True, null=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
            return self.product_title