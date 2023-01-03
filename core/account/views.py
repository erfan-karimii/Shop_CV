from django.shortcuts import render,redirect
from .forms import PhoneNumber
from kavenegar import *
from django.contrib.auth import get_user_model
import random
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
    number = random.randint(1000, 9999)
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
            messages.success(request,'درست وارد کنید')
            return render(request,'account/register.html')
    else :
        return render(request,'account/register.html')


def VerifyChecked(request):
    if request.method == "POST":
        token = request.POST.get('token')
        phone_c = request.COOKIES['phone_number_cookie']
        #----------------------------------------
        try :
            user = MyUser.objects.get(phone_number= phone_c)
        except:
            messages.success(request,'شما اکانتی با این شماره ندارید')
        if user.token == token :
            MyUser.objects.filter(phone_number=phone_c).update(is_verified=True)
            return render(request,'account/complateprofile.html')
        else :
            messages.success(request,'کدارسالی را درست وارد کنید')
        return redirect('/')
    return render(request,'account/complateprofile.html')


def ComplateProfileView(request):
    return render(request,'account/complateprofile.html',{})


def ComplateProfile(request):
    if request.method == "POST":
        # username=request.POST.get('username')
        password = request.POST.get('password')
        phone_c = request.COOKIES['phone_number_cookie']
        MyUser.objects.filter(phone_number=phone_c).update(
            phone_number=phone_c,password=make_password(password)
        )
        messages.success(request,'پروفایل شما با موفقیت ساخته شد')
        user = MyUser.objects.get(phone_number=phone_c)
        if user.is_verified:
            login(request, user)
    return redirect('/')


def respass(request):
    return render(request,'account/eghdam.html')


def SendSmsReset(request):
    number = random.randint(1000, 9999)
    print(number)
    if request.method == "POST":
        phone_number = request.POST.get('phone_number')
        if MyUser.objects.filter(phone_number=phone_number):
            MyUser.objects.filter(phone_number=phone_number).update(token=number)
        else:
            messages.success(request,'شما هیج اکانتی ندارید')
    else:
        return render(request,'account/verify2.html')

    # api = KavenegarAPI('4D526E3432522F42744D47414B3845436D59734377572B71645A455565644575')
    # params = {'sender' : '10000080808880', 'receptor': f'{phone}', 'message' :f'{number}' }
    # api.sms_send( params)
    response = render(request,'account/verify2.html')
    x =phone_number
    response.set_cookie('phone_number_cookie',x,1000)
    return response


def ResetProfileView(request):
    return render(request,'account/ResetPasswordView.html',{})


def ResetProfile(request):
    if request.method == "POST":
        # username=request.POST.get('username')
        password = request.POST.get('password')
        phone_c = request.COOKIES['phone_number_cookie']
        MyUser.objects.filter(phone_number=phone_c).update(
            password=make_password(password)
        )
        messages.success(request,'عملیات با موفقیت انجام شد')
    return redirect('/')


def VerifyChecked2(request):
    if request.method == "POST":
        token = request.POST.get('token')
        phone_c = request.COOKIES['phone_number_cookie']
        try :
            user = MyUser.objects.get(phone_number= phone_c)
        except:
            messages.success(request,'شما اکانتی با این شماره ندارید')

        if user.token == token :
            return render(request,'account/ResetPasswordView.html')
        else:
            messages.success(request,'!!! کدارسالی را درست وارد کنید')
        return redirect('account/ResetPasswordView.html')
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
                return redirect('/')
            else:
                messages.success(request,"شما احراز هویت نشده ایید")
    form = AuthenticationForm()
    return render(request,'account/login.html',{'form':form})

def LogOut(request):
    logout(request)
    return redirect('/')