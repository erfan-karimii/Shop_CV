from django.shortcuts import render
from .models import SiteSetting,NavOne,Slider,Tabligh,FooterOne , OnSale
from product.models import Product 
# Create your views here.

def index_view(request):
    context = {
        'Sliders':Slider.objects.all(),
        'tabligh_right':Tabligh.objects.get(diraction='right'),
        'tabligh_left':Tabligh.objects.get(diraction='left'),
        'tabligh_right2':Tabligh.objects.get(diraction='right2'),
        'SiteSetting':SiteSetting.objects.filter(active=True).last(),
        'latest_products' : Product.objects.all().order_by('-created'),
        'on_sale' : OnSale.objects.filter(is_show=True).last(),
    }
    return render(request,'index.html',context)


def header_view(request):
    context = {
        'NavOne':NavOne.objects.all(),
        'SiteSetting':SiteSetting.objects.filter(active=True).last(),
    }
    return render(request,'header.html',context)

def footer_view(request):
    context = {
        'FooterOne':FooterOne.objects.all(),
        'SiteSetting':SiteSetting.objects.filter(active=True).last(),
    }
    return render(request,'footer.html',context)