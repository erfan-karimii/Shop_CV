from django import forms
from .models import WishList

class WishListForm(forms.ModelForm):
    class Meta:
        model = WishList
        fields = '__all__'
