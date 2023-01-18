from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
import requests
import json
import datetime
from cart.models import Order,OrderDetail
from cart.views import total_priceCA
from product.models import Product

MERCHANT = '9fcdf799-adcd-42aa-99c0-35169d838586'
ZP_API_REQUEST = "https://api.zarinpal.com/pg/v4/payment/request.json"
ZP_API_VERIFY = "https://api.zarinpal.com/pg/v4/payment/verify.json"
ZP_API_STARTPAY = "https://www.zarinpal.com/pg/StartPay/{authority}"
amount = 10000  # Rial / Required
description = "توضیحات مربوط به تراکنش را در این قسمت وارد کنید"  # Required
email = 'h410mi3@gmail.com'  # Optional
mobile = '09024485880'  # Optional
# Important: need to edit for realy server.
CallbackURL = 'http://localhost:8000/verify/'


def send_request(request):
    c = request.COOKIES['OrderDetail']
    cookie = json.loads(c)
    amount = 0
    for key , value in cookie.items():
        price = total_priceCA(value['id'],value['color'],value['size'])
        amount += price
    amount = amount *10
    req_data = {
        "merchant_id": MERCHANT,
        "amount": amount,
        "callback_url": CallbackURL,
        "description": description,
        "metadata": {"mobile": mobile, "email": email}
    }
    req_header = {"accept": "application/json",
                  "content-type": "application/json'"}
    req = requests.post(url=ZP_API_REQUEST, data=json.dumps(
        req_data), headers=req_header)
    authority = req.json()['data']['authority']
    if len(req.json()['errors']) == 0:
        return redirect(ZP_API_STARTPAY.format(authority=authority))
    else:
        e_code = req.json()['errors']['code']
        e_message = req.json()['errors']['message']
        return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")


def verify(request):
    c = request.COOKIES['OrderDetail']
    cookie = json.loads(c)
    amount = 0
    for key , value in cookie.items():
        price = total_priceCA(value['id'],value['color'],value['size'])
        amount += price
    amount = amount *10
    t_status = request.GET.get('Status')
    t_authority = request.GET['Authority']
    if request.GET.get('Status') == 'OK':
        req_header = {"accept": "application/json",
                      "content-type": "application/json'"}
        req_data = {
            "merchant_id": MERCHANT,
            "amount": amount,
            "authority": t_authority
        }
        req = requests.post(url=ZP_API_VERIFY, data=json.dumps(req_data), headers=req_header)
        if len(req.json()['errors']) == 0:
            t_status = req.json()['data']['code']
            if t_status == 100:
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
                
                REFID=req.json()['data']['ref_id']
                messages.success(request, f'خرید شما با موفقیت ثبت شد\nREFID:{REFID}')
                response = redirect('home:open_old_cart')
                response.set_cookie('OrderDetail',{},72*60*60)
                response.delete_cookie('Order')
                response.delete_cookie('information')
                return response
            elif t_status == 101:
                return HttpResponse('Transaction submitted : ' + str(
                    req.json()['data']['message']
                ))
            else:
                return HttpResponse('Transaction failed.\nStatus: ' + str(
                    req.json()['data']['message']
                ))
        else:
            e_code = req.json()['errors']['code']
            e_message = req.json()['errors']['message']
            return HttpResponse(f"Error code: {e_code}, Error Message: {e_message}")
    else:
        messages.error(request, f'خرید با مشکل مواجه شد یا از طریق کاربر کنسل شد.')
        response = redirect('cart:user_open_order')
        response.delete_cookie('information')
        return response
