from django.shortcuts import render
from .models import SiteSetting,NavOne,NavTwo,Slider,Tabligh,FooterOne,FooterTwo
# Create your views here.

def index_view(request):
    context = {
        'Sliders':Slider.objects.all(),
        'Tablighs':Tabligh.objects.all(),
        'SiteSetting':SiteSetting.objects.filter(active=True).last(),
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