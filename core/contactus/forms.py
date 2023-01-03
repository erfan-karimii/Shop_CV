from django import forms
from .models import ContactUsKeeper , Newsletter

class ContactUsKeeperForm(forms.ModelForm):
    class Meta:
        model = ContactUsKeeper
        fields = '__all__'

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = '__all__'