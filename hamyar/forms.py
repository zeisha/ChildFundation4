from django import forms
from .models import Hamyar


class HamyarForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Hamyar
        fields = ['country', 'city', 'address',
                  'postal_code', 'phone_number']
