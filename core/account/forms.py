from django import forms 
import re

class PhoneNumber(forms.Form):
    phone_number = forms.RegexField(regex=r'^(?:0|98|\+98|\+980|0098|098|00980)?(9\d{9})$')

