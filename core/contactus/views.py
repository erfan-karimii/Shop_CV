from django.shortcuts import render , redirect
from django.contrib import messages
from django.http import HttpResponseRedirect

from home.models import SiteSetting
from .models import ContactUsKeeper ,Newsletter
from .forms import ContactUsKeeperForm , NewsletterForm

# Create your views here.
def contact_us_view(request):
    context = {
        "SiteSetting": SiteSetting.objects.filter(active=True).last()
    }
    return render(request,'contact.html',context)

def validate_contact_us(request):
    if request.method == 'POST':
        form = ContactUsKeeperForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'.پیام شما با موفقیت دریافت شد')
        else :
            messages.error(request,'.متاسفانه مشکلی رخ داده است لطفا دوباره تلاش کنید')
        return redirect('contactus:contact-us')

def validate_newsletter(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'ایمیل شما با موفقیت ثبت شد.')
        else :
            if 'Email already exists' in str(form.errors):
                messages.error(request, 'این ایمیل قبلا ثبت شده است')
            elif 'Enter a valid email address' in str(form.errors):                
                messages.error(request, 'ظاهرا مشکلی پیش امده است لطفا دوباره امتحان کنید.')
        return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))