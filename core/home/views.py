from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse 
from .models import SiteSetting,NavOne,Slider,Tabligh,FooterOne , OnSale , WishList
from product.models import Product ,Category
from account.models import Profile
from django.contrib import messages
from cart.models import OrderDetail
from django.db.models import Sum
import json

# Create your views here.

def index_view(request):
    context = {
        'Sliders':Slider.objects.all(),
        'tabligh_right':Tabligh.objects.filter(diraction='right').last(),
        'tabligh_left':Tabligh.objects.filter(diraction='left').last(),
        'tabligh_right2':Tabligh.objects.filter(diraction='right2').last(),
        'SiteSetting':SiteSetting.objects.filter(active=True).last(),
        'latest_products' : Product.objects.filter(is_active=True).order_by('-created'),
        'pants' : Product.objects.filter(category__name = 'شلوار'),
        'shirts' : Product.objects.filter(category__name = 'پیراهن'),
        'man_clothes' : Product.objects.filter(category__name = 'لباس مردانه'),
        'woman_clothes' : Product.objects.filter(category__name = 'لباس زنانه'),
        'on_sale_section' : OnSale.objects.filter(is_show=True).last(),
    }
    return render(request,'index.html',context)

def header_view(request):
    wishlist_count = 0
    if request.user.is_authenticated:
        wishlist_count = WishList.objects.filter(account__user=request.user).count()
    try:
        detail = request.COOKIES['OrderDetail']
        count = json.loads(detail)
        count = len(count)
    except :
        count = 0

    context = {
        'NavOne':NavOne.objects.all(),
        'SiteSetting':SiteSetting.objects.filter(active=True).last(),
        'wishlist_count' : wishlist_count,
        'categories':Category.objects.all(),
        'count':count ,
    }
    return render(request,'layout/header.html',context)

def footer_view(request):
    context = {
        'FooterOne':FooterOne.objects.all(),
        'SiteSetting':SiteSetting.objects.filter(active=True).last(),
    }
    return render(request,'layout/footer.html',context)

def quick_view(request,id):
    product = Product.objects.get(id=id)
    context = {
        'id' : product.id,
        'category' : product.category.name,
        'name' : product.name,
        'price' : product.main_discount_call(),
        'info' : product.info[:360],
        'image' : product.image.url,
    }
    return  JsonResponse(context)

@login_required(login_url='/account/login/')
def add_to_wishlist(request,user,product_id,color,size):
    product = Product.objects.get(id=product_id)
    profile = Profile.objects.get(user__phone_number=user)
    state = WishList.objects.get_or_create(product=product,account=profile,color=color,size=size)
    if state[1]:
        messages.success(request,'محصول به لیست علاقه مندی شما اضافه شد')
    else:
        messages.error(request,'محصول قبلا به لیست شما اضافه شده است')
    return redirect('home:wishlist')

@login_required(login_url='/account/login/')
def add_to_wishlist_ajax(request,user,product_id,color,size):
    product = Product.objects.get(id=product_id)
    profile = Profile.objects.get(user__phone_number=user)
    state = WishList.objects.get_or_create(product=product,account=profile,color="#"+color,size=size)
    return JsonResponse({"state":state[1]})


@login_required(login_url='/account/login/')
def wishlist_view(request):
    wishlist = WishList.objects.filter(account__user=request.user)
    context = {
        'wishlist': wishlist
    }
    return render(request,'wishlist.html',context)

@login_required(login_url='/account/login/')
def wishlist_delete_item(request,id):
    wish_item = WishList.objects.get(id=id)
    wish_item.delete()
    messages.success(request,'محصول از علاقه مندی های شما حذف شد')
    return redirect('home:wishlist')

def compare_view(request):
    return render(request,'compare.html',{})

def compare_view_2(request,id):
    product_1 = Product.objects.get(id=id)
    context = {
        'product_1' : product_1,
        'id_1':id
    }
    return render(request,'compare.html',context)

def compare_listview(request,cat,id_1):
    # check = Product.objects.get(id=id_1).category
    # if cat != check:
    #     raise Http404
    posts = Product.objects.filter(category__name=cat,is_active=True,).order_by('-instock','-created')
    context = {
        'posts':posts,
        'id_1':id_1,
        'cat':cat,
        }
    return render(request,'compare_listview.html',context)

def compare_view_3(request,id_1,id_2):
    product_1 = Product.objects.get(id=id_1)
    product_2 = Product.objects.get(id=id_2)
    context = {
        'product_1' : product_1,
        'product_2' : product_2,
    }
    return render(request,'compare.html',context)

