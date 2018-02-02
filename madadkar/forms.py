from django import forms
from .models import Madadkar


class HamyarForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = Madadkar
        fields = ['country', 'city', 'address',
                  'postal_code', 'phone_number']
