from django import forms
from .models import *


# class HamyarForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput)
#
#     class Meta:
#         model = Hamyar
#         fields = ['country', 'city', 'address',
#                   'postal_code', 'phone_number']

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['value', 'kind']

class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ['content']

class PaymentFoundationForm(forms.ModelForm):
    class Meta:
        model = PaymentFoundation
        fields = ['value']
