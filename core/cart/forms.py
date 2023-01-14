from django import forms


class NewOrderForm(forms.Form):
    product_id = forms.IntegerField(widget=forms.HiddenInput())
    size = forms.CharField(max_length=20)
    color = forms.CharField(max_length=7)
    count = forms.IntegerField(
        widget = forms.NumberInput(),
        initial=1
    )
