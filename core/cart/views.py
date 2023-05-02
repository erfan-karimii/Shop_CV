from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import JsonResponse , Http404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum ,F
import json
import copy
import datetime

from .models import Order,OrderDetail
from product.models import Product
from .forms import NewOrderForm

# Create your views here.

def get_order_id(request):
    x = Order.objects.create()
    y = copy.copy(x.id)
    x.delete()
    return JsonResponse({'order_id':y})

def total_priceCA(product_id,color,size):
    price_color = 0
    product = Product.objects.get(id=product_id)
    try:
        x = product.color_set.get(color=color)
        price_color = x.Ekhtelaf
    except:
        if product.orgin_color != color:
            raise Http404
    price_size = 0
    try:
        x = product.size_set.get(size=size)
        price_size = x.Ekhtelaf
    except:
        if product.orgin_size != size:
            raise Http404
    return price_color + price_size + product.main_discount_call()

def add_user_order(request):
    form = NewOrderForm(request.POST or None)
    if form.is_valid():
        product_id =form.cleaned_data['product_id']    
        product = Product.objects.get(id=product_id)
        color = form.cleaned_data['color']
        size =form.cleaned_data['size']
        count = form.cleaned_data['count']
        if count < 1 or count > product.product_count : 
            return redirect('/')
        
        total_price = total_priceCA(product_id,color,size)

        x = request.COOKIES['OrderDetail']
        y = request.COOKIES['Order']
        jsonstyle = json.loads(x)
        order = Order.objects.create(id=y)
        orderdetail = OrderDetail.objects.create(order=order,product=product,color=color,orderdetail_count=count,size=size,price=total_price)
        order.delete()

        for x in jsonstyle:
            if jsonstyle[x]['id'] == product_id and jsonstyle[x]['color'] == color and jsonstyle[x]['size'] == size:
                jsonstyle[x] = {'id':product_id,'color':color,'size':size,'count':count}
                break
        else:
            jsonstyle[orderdetail.id] = {'id':product_id,'color':color,'size':size,'count':count}

        orderdetail.delete()
        jsonstyle2 = json.dumps(jsonstyle)
        response = redirect('/cart/')
        response.delete_cookie('OrderDetail')
        response.set_cookie('OrderDetail',jsonstyle2,172800)
        return response 
    else:
        return redirect('/')

def user_open_order(request):
    total_price = 0
    details = json.loads(request.COOKIES['OrderDetail'])
    for det in details:
        id = details[det]['id']
        product = Product.objects.get(id=id)
        if details[det]['count'] > product.product_count:
            details[det]['count'] = product.product_count

        total_price_single = total_priceCA(details[det]['id'],details[det]['color'],details[det]['size'])
        total_price += total_price_single * details[det]['count']

    context = {
    'details':details,
    'total':total_price,
    }
    return render(request,'cart.html',context) 

def remove_from_cookie(request,id):
    order_detail = request.COOKIES['OrderDetail']
    f = json.loads(order_detail)
    del f[id]
    m = json.dumps(f)
    messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
    response = redirect('/cart')
    response.delete_cookie('OrderDetail')
    response.set_cookie('OrderDetail',m,172800)
    return response

def update_In_open_order(request):
    form = NewOrderForm(request.POST or None)
    if form.is_valid():
        product_id =form.cleaned_data['product_id']    
        product = Product.objects.get(id=product_id)
        color = form.cleaned_data['color']
        size =form.cleaned_data['size']
        count = form.cleaned_data['count']

        if count < 1 or count > product.product_count :
            messages.error(request, 'متاسقانه مشکلی پیش امئه است لطفا دوباره امتحان کنید.')
            return redirect('/cart/')
        

        x = request.COOKIES['OrderDetail']
        jsonstyle = json.loads(x)

        for x in jsonstyle:
            if jsonstyle[x]['id'] == product_id and jsonstyle[x]['color'] == color and jsonstyle[x]['size'] == size:
                jsonstyle[x] = {'id':product_id,'color':color,'size':size,'count':count}
        
        jsonstyle2 = json.dumps(jsonstyle)
        messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
        response = redirect('/cart')
        response.delete_cookie('OrderDetail')
        response.set_cookie('OrderDetail',jsonstyle2,172800)
        return response

@login_required(login_url='account:login')
def check_out_view(request):
    details = request.COOKIES['OrderDetail']
    context = {
        'details': json.loads(details),
    }
    return render(request,'checkout.html',context)

def how_user_pay(request):
    payment_method = request.POST.get('payment_method')
    if payment_method == 'cash':
        c = request.COOKIES['OrderDetail']
        cookie = json.loads(c)

        order_id = request.COOKIES['Order']
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')

        if not full_name or not address or not phone_number:
            return redirect('/')
        
        order = Order.objects.create(id=order_id,owner=request.user,full_name=full_name,address=address,\
            phone_number=phone_number,is_paid=True,payment_date=datetime.datetime.now())
        for key , value in cookie.items():
            product = Product.objects.get(id=value['id'])
            product.product_count -= value['count']
            product.save()
            price = total_priceCA(value['id'],value['color'],value['size'])
            OrderDetail.objects.create(id=key,order=order,product=product,price=price,color=value['color'],\
                size=value['size'],orderdetail_count=value['count'])

        messages.success(request,'خرید شما با موفقیت انجام شد.')
        response = redirect('cart:home')
        response.set_cookie('OrderDetail',{},72*60*60)
        response.delete_cookie('Order')
        return response

    elif payment_method == 'pay_online':
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        if not full_name or not address or not phone_number:
            return redirect('/')
        information = {"address":address,"full_name":full_name,"phone_number":phone_number}
        jsonstyle = json.dumps(information)
        response = redirect('zarinpal:request')
        response.set_cookie('information',jsonstyle,72*60*60)
        return response
    else : 
        messages.error(request,'متاسفانه مشکلی پیش امده است لطفا دوباره امتحان کنید.')
        return redirect('cart:check_out')

@login_required(login_url='account:login')
def open_old_cart(request):
    user = request.user
    carts = Order.objects.filter(is_paid=True,owner=user).order_by('-payment_date')
    context = {
        'carts' : carts,
    }
    return render(request,'old_cart.html',context)

@login_required(login_url='account:login')
def open_old_orderdetail(request,id):
    order = Order.objects.get(id=id,is_paid=True)
    orderdetails = OrderDetail.objects.filter(order=order)
    total = orderdetails.aggregate(total_price=Sum(F('price') * F('orderdetail_count')))
    context = {
        'order' : order,
        'details' : orderdetails,
        'total' : total['total_price'],
    }
    return render(request,'old_cart_details.html',context)
