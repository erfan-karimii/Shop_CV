from django.shortcuts import render
from .models import AboutUsGeneral , AboutUsProperty , AboutUsProgressBar
# Create your views here.

def about_us_view(request):
    context = {
        'AboutUsGeneral' : AboutUsGeneral.objects.filter(active=True).last(),
        'AboutUsProperty' : AboutUsProperty.objects.all(),
        'AboutUsProgressBar' : AboutUsProgressBar.objects.all(), 
    }
    return render(request,'about.html',context)

