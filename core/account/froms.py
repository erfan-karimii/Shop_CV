from django import forms 

class PhoneNumber(forms.Form):
    phone_number = forms.CharField()

