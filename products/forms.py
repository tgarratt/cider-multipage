from django import forms
from .models import add_bottle, add_crate, add_keg


class add_bottle_form(forms.ModelForm):
    class Meta:
        model = add_bottle
        fields = (
            'product_type', 'bottle_title', 'bottle_price', 'bottle_img', 'featured')



class add_crate_form(forms.ModelForm):
    class Meta:
        model = add_crate
        fields = (
            'crate_title', 'crate_price', 'crate_img')



class add_keg_form(forms.ModelForm):
    class Meta:
        model = add_keg
        fields = (
            'keg_title', 'keg_price', 'keg_img')