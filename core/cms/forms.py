from django import forms
from product.models import Product , Size , Color , GalleryImage

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
            'tozihat' : forms.TextInput(attrs={'class': 'form-control'}),
            'alt' : forms.TextInput(attrs={'class': 'form-control'}),
            'alt_2' : forms.TextInput(attrs={'class': 'form-control'}),
            'orgin_size' : forms.TextInput(attrs={'class': 'form-control'}),
            'price' : forms.NumberInput(attrs={'class': 'form-control'}),
            'product_count' : forms.NumberInput(attrs={'class': 'form-control'}),
            'discount' : forms.NumberInput(attrs={'class': 'form-control','max':100,'min':0}),
        }

class ColorForm(forms.ModelForm):
    class Meta:
        model = Color
        fields = '__all__'
        widgets = {
            'Ekhtelaf': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class SizeForm(forms.ModelForm):
    class Meta:
        model = Size
        fields = '__all__'
        widgets = {
            'Ekhtelaf': forms.NumberInput(attrs={'class': 'form-control'}),
            'size': forms.TextInput(attrs={'class': 'form-control'}),
        }

class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = '__all__'
        widgets = {
            'alt': forms.TextInput(attrs={'class': 'form-control'}),
        }