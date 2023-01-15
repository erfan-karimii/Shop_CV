from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.utils import timezone
from django.http import JsonResponse , HttpResponse
from django.contrib.auth.decorators import login_required
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
        pass
    price_size = 0
    try:
        x = product.size_set.get(size=size)
        price_size = x.Ekhtelaf
    except:
        pass
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
        orderdetail = OrderDetail.objects.create(order=order,product=product,color=color,count=count,size=size,price=total_price)
        order.delete()

        for x in jsonstyle:
            if jsonstyle[x]['id'] == product_id and jsonstyle[x]['color'] == color and jsonstyle[x]['size'] == size:
                jsonstyle[x] = {'id':product_id,'color':color,'size':size,'count':count}
                break
        else:
            jsonstyle[orderdetail.id] = {'id':product_id,'color':color,'size':size,'count':count}

        orderdetail.delete()
        jsonstyle2 = json.dumps(jsonstyle)
        response = redirect('/cart')
        response.delete_cookie('OrderDetail')
        response.set_cookie('OrderDetail',jsonstyle2,172800)
        return response 

    else:
        return redirect('/')

def user_open_order(request):
    context = {
    'order':None,
    'details':None,
    'total':0,
    'sum':0,
    }
    total_price = 0
    detail = request.COOKIES['OrderDetail']
    z = json.loads(detail)
    print(z)
    for det in z:
        id = z[det]['id']
        product = Product.objects.get(id=id)
        if z[det]['count'] > product.product_count:
            z[det]['count'] = product.product_count

        total_price_single = total_priceCA(z[det]['id'],z[det]['color'],z[det]['size'])
        total_price += total_price_single * z[det]['count']

    context['details'] = z
    context['total'] = total_price

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
        
        
        total_price = total_priceCA(product_id,color,size)

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
        o = request.COOKIES['Order']
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        if not full_name or not address or not phone_number:
            return redirect('/')
        order = Order.objects.create(id=o,owner=request.user,full_name=full_name,address=address,\
            phone_number=phone_number,is_paid=True,payment_date=datetime.datetime.now())
        for key , value in cookie.items():
            product = Product.objects.get(id=value['id'])
            product.product_count -= value['count']
            product.save()
            price = total_priceCA(value['id'],value['color'],value['size'])
            OrderDetail.objects.create(id=key,order=order,product=product,price=price,color=value['color'],\
                size=value['size'],count=value['count'])

        messages.success(request,'خرید شما با موفقیت انجام شد.')
        response = redirect('home:home')
        response.set_cookie('OrderDetail',{},72*60*60)
        response.delete_cookie('Order')
        return response

    elif payment_method == 'pay_online':
        return HttpResponse('done')
    else : 
        messages.error(request,'متاسفانه مشکلی پیش امده است لطفا دوباره امتحان کنید.')
        return redirect('cart:check_out')

    

