from django import forms 
import re

class PhoneNumber(forms.Form):
    phone_number = forms.IntegerField()



    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        if not re.match(r'^(?:0|98|\+98|\+980|0098|098|00980)?(9\d{9})$', str(phone_number)):
            raise forms.ValidationError("شماره تلفن را درست وارد کنید")
        return phone_number