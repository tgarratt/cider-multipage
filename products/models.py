from django.db import models


class add_bottle(models.Model):

    bottle_title = models.CharField(max_length=50, blank=False)
    bottle_price = models.DecimalField(blank=False, max_digits=10, decimal_places=2)
    bottle_img = models.ImageField(upload_to="static/img", blank=True, null=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
            return self.bottle_title



class add_crate(models.Model):

    crate_title = models.CharField(max_length=50, blank=False)
    crate_price = models.DecimalField(blank=False, max_digits=10, decimal_places=2)
    crate_img = models.ImageField(upload_to="static/img", blank=True, null=True)

    def __str__(self):
            return self.crate_title



class add_keg(models.Model):

    keg_title = models.CharField(max_length=50, blank=False)
    keg_price = models.DecimalField(blank=False, max_digits=10, decimal_places=2)
    keg_img = models.ImageField(upload_to="static/img", blank=True, null=True)

    def __str__(self):
            return self.keg_title