from django import forms
from .models import add_product


class add_product_form(forms.ModelForm):
    class Meta:
        model = add_product
        fields = (
            'product_type', 'product_title', 'product_price', 'product_img', 'featured')

