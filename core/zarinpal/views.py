from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings

import time
import requests
import json
import datetime
from cart.models import Order,OrderDetail
from cart.views import total_priceCA
from product.models import Product

#? sandbox merchant 
sandbox = 'sandbox'


MERCHANT = '9fcdf799-adcd-42aa-99c0-35169d838586'
ZP_API_REQUEST = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentRequest.json"
ZP_API_VERIFY = f"https://{sandbox}.zarinpal.com/pg/rest/WebGate/PaymentVerification.json"
ZP_API_STARTPAY = f"https://{sandbox}.zarinpal.com/pg/StartPay/"

amount = 10000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'h410mi3@gmail.com'  # Optional
mobile = '09024485880'  # Optional
# Important: need to edit for realy server.
if settings.DEBUG:
    CallbackURL = 'http://localhost:8000/verify/'
else:
    CallbackURL = ''

def send_request(request):
    c = request.COOKIES['OrderDetail']
    cookie = json.loads(c)
    amount = 0
    for key , value in cookie.items():
        price = total_priceCA(value['id'],value['color'],value['size'])
        amount += price
    amount = amount * 10
    data = {
        "MerchantID": MERCHANT,
        "Amount": amount,
        "Description": description,
        "Phone": mobile,
        "CallbackURL": CallbackURL,
    }
    data = json.dumps(data)

    headers = {'content-type': 'application/json', 'content-length': str(len(data)) }

    try:
        response = requests.post(ZP_API_REQUEST, data=data,headers=headers, timeout=10)
        if response.status_code == 200:
            response = response.json()
            if response['Status'] == 100:
                return redirect(ZP_API_STARTPAY + str(response['Authority']))
        return redirect('/')
    
    except requests.exceptions.Timeout:
        return {'status': False, 'code': 'timeout'}
    except requests.exceptions.ConnectionError:
        return {'status': False, 'code': 'connection error'}


def verify(request):
    c = request.COOKIES['OrderDetail']
    cookie = json.loads(c)
    amount = 0
    for key , value in cookie.items():
        price = total_priceCA(value['id'],value['color'],value['size'])
        amount += price
    amount = amount *10
    data = {
    "MerchantID": MERCHANT,
    "Amount": amount,
    "Authority": request.GET.get('Authority'),
    }
    data = json.dumps(data)
    headers = {'content-type': 'application/json', 'content-length': str(len(data)) }
    response = requests.post(ZP_API_VERIFY, data=data,headers=headers)
    if response.status_code == 200:
        response = response.json()
        if response['Status'] == 100 or response['Status'] == 101:
            order_id = request.COOKIES['Order']
            information = request.COOKIES['information']
            jsonstyle = json.loads(information)
            full_name = jsonstyle['full_name']
            address = jsonstyle['address']
            phone_number = jsonstyle['phone_number']

            order = Order.objects.create(id=order_id,owner=request.user,full_name=full_name,address=address,\
                phone_number=phone_number,is_paid=True,payment_date=datetime.datetime.now())
            
            for key , value in cookie.items():
                product = Product.objects.get(id=value['id'])
                product.product_count -= value['count']
                product.save()
                price = total_priceCA(value['id'],value['color'],value['size'])
                OrderDetail.objects.create(id=key,order=order,product=product,price=price,color=value['color'],\
                    size=value['size'],orderdetail_count=value['count'])
            
            messages.success(request, f'خرید شما با موفقیت ثبت شد')
            response = redirect('cart:open_old_cart')
            response.set_cookie('OrderDetail',{},72*60*60)
            response.delete_cookie('Order')
            response.delete_cookie('information')
            return response
        else:
            messages.error(request,'خرید با مشکل مواجه شد یا از طریق کاربر کنسل شد.')
            response = redirect('cart:user_open_order')
            response.delete_cookie('information')
            return response
    else:
        e_code = response['errors']['code']
        e_message = response['errors']['message']
        return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
        