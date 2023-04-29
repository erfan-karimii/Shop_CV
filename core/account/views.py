from django.shortcuts import render,redirect
from .forms import PhoneNumber
from kavenegar import *
from django.contrib.auth import get_user_model
import random
import string
from django.contrib.auth.hashers import make_password
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.auth import login,logout
# Create your views here.

MyUser = get_user_model()

def registerView(request):
    if request.user.is_authenticated:
        return redirect('/')
    return render(request,'account/register.html',{})

def send_sms_test(request):
    number = random.randint(1000, 99999)
    if request.method == "POST":
        form=PhoneNumber(request.POST)
        if form.is_valid():

            phone_number =form.cleaned_data['phone_number']
            if MyUser.objects.filter(phone_number=phone_number):
                MyUser.objects.filter(phone_number=phone_number).update(token=number)
            else:
                MyUser.objects.create(phone_number=phone_number,token=number)
            print(number)

            # api = KavenegarAPI('4D526E3432522F42744D47414B3845436D59734377572B71645A455565644575')
            # params = { 'sender' : '10000080808880', 'receptor': f'{phone_number}', 'message' :f'{number}' }
            # try:
            #     api.sms_send( params)
            # except:
            #     messages.success(request,'درست وارد کنید')
            #     return render(request,'account/register.html')

            response = render(request,'account/verify.html')
            
            response.set_cookie('phone_number_cookie',phone_number,1000)
            return response
        else:
            messages.error(request,'شماره همراه خود را درست وارد کنید')
            return redirect('account:registerView')
    else :
        return redirect('account:registerView')

def VerifyChecked(request):
    if request.method == "POST":
        token = request.POST.get('token')
        try :
            phone_c = request.COOKIES['phone_number_cookie']
            user = MyUser.objects.get(phone_number= phone_c)
        except KeyError:
            messages.error(request,'زمان احراز هویت شما به پایان رسیده است ')
            return redirect('account:registerView')
        if user.token == token :
            MyUser.objects.filter(phone_number=phone_c).update(is_verified=True)
            return redirect('account:complate')
        else :
            messages.error(request,'کدارسالی را درست وارد کنید')
            return redirect('account:verify')
    else:
        return render(request,'account/verify.html')

def ComplateProfile(request):
    if request.method == "POST":
        try:
            phone_c = request.COOKIES['phone_number_cookie']
        except KeyError:
            messages.error(request,'زمان احراز هویت شما به پایان رسیده است ')
            return redirect('account:registerView')
        password = request.POST.get('password','@#$12345random%^&*1234')
        user = MyUser.objects.get(phone_number=phone_c)
        user.set_password(password)
        user.save()
        messages.success(request,'پروفایل شما با موفقیت ساخته شد')
        user = MyUser.objects.get(phone_number=phone_c)
        if user.is_verified:
            login(request, user)
            return redirect('/')
    else:
        return render(request,'account/complateprofile.html',{})


# TODO : use kavenegar api
def SendSmsReset(request):
    number = random.randint(1000, 9999)
    print(number)
    if request.method == "POST":
        form = PhoneNumber(request.POST)
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
        else:
            messages.error(request,"اطلاعات ورودی صحیح نمیباشد")
            return redirect('account:send2')
        if MyUser.objects.filter(phone_number=phone_number):
            MyUser.objects.filter(phone_number=phone_number).update(token=number)
            response = render(request,'account/verify2.html')
            response.set_cookie('phone_number_cookie',phone_number,1000)
            return response
        else:
            messages.error(request,'شما هیج اکانتی ندارید')
            return redirect('account:send2')
    else:
        return render(request,'account/eghdam.html')

def ResetProfile(request):
    if request.method == "POST":
        # username=request.POST.get('username')
        password = request.POST.get('password')
        try :
            phone_c = request.COOKIES['phone_number_cookie']
        except:
            messages.error(request,'زمان احراز هویت شما به پایان رسیده است')
            return redirect('account:send2')
        MyUser.objects.filter(phone_number=phone_c).update(
            password=make_password(password)
        )
        messages.success(request,'عملیات با موفقیت انجام شد')
    return redirect('/')

def VerifyChecked2(request):
    if request.method == "POST":
        token = request.POST.get('token')
        try :
            phone_c = request.COOKIES['phone_number_cookie']
            user = MyUser.objects.get(phone_number= phone_c)
        except:
            messages.error(request,'شما اکانتی با این شماره ندارید')
            return redirect('account:send2')

        if user.token == token :
            return render(request,'account/ResetPasswordView.html')
        else:
            messages.error(request,'!!! کدارسالی را درست وارد کنید')
            return redirect('account:changepass')
    return render(request,'account/ResetPasswordView.html')

def Login(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.is_verified:
                login(request, user)
                messages.success(request,'شما با موفقیت وارد حساب کاربری خود شدید')
                return redirect('/')
            else:
                messages.error(request,"شما احراز هویت نشده ایید")
        else:
            messages.error(request,'شماره همراه یا رمز عبور اشتباه است')
    form = AuthenticationForm()
    return render(request,'account/login.html',{'form':form})

def LogOut(request):
    logout(request)
    messages.success(request,"شما با موفقیت از حساب کاربری خود خارج شدید")
    return redirect('/')
