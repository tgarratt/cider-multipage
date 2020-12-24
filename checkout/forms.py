from django import forms
from django.utils import timezone


#  Required fields for stripe
class payment_form(forms.Form):

    now = timezone.now()
    current_year = now.year

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(current_year, 2041)]

    credit_card_number = forms.CharField(
        initial=4242424242424242, max_length=19, label='Credit card number', required=False, disabled="disabled")
    cvv = forms.CharField(initial=222, max_length=3, min_length=3, label='Security code', required=False, disabled="disabled")
    expiry_month = forms.ChoiceField(
        label='Expiry Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(
        label='Expiry Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)