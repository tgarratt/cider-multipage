from django import forms
from .models import CheckoutUserInfo

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]

class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
                                choices=PRODUCT_QUANTITY_CHOICES,
                                coerce=int)
    update = forms.BooleanField(required=False,
                                initial=False,
                                widget=forms.HiddenInput)
                                

class CheckoutUserInfoForm(forms.ModelForm):
    class Meta:
        model = CheckoutUserInfo
        fields = (
            'user_email', 'user_name', 'user_country',
             'user_city', 'user_line1', 'user_line2',
              'user_postcode', 'user_countystate')    