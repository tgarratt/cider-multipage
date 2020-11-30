from django import forms
from django.utils import timezone


#  Required fields for stripe
class payment_form(forms.Form):

    now = timezone.now()
    current_year = now.year

    MONTH_CHOICES = [(i, i) for i in range(1, 13)]
    YEAR_CHOICES = [(i, i) for i in range(current_year, 2041)]

    credit_card_number = forms.CharField(
        max_length=19, label='Credit card number', required=False)
    cvv = forms.CharField(max_length=3, label='Security code', required=False)
    expiry_month = forms.ChoiceField(
        label='Month', choices=MONTH_CHOICES, required=False)
    expiry_year = forms.ChoiceField(
        label='Year', choices=YEAR_CHOICES, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)