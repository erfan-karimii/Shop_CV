from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import SiteSetting,NavOne,Slider,Tabligh,FooterOne , OnSale , WishList
from product.models import Product 
from django.contrib import messages

# Create your views here.

def index_view(request):
    context = {
        'Sliders':Slider.objects.all(),
        'tabligh_right':Tabligh.objects.get(diraction='right'),
        'tabligh_left':Tabligh.objects.get(diraction='left'),
        'tabligh_right2':Tabligh.objects.get(diraction='right2'),
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
    wishlist_count = WishList.objects.filter(account__user=request.user).count()

    context = {
        'NavOne':NavOne.objects.all(),
        'SiteSetting':SiteSetting.objects.filter(active=True).last(),
        'wishlist_count' : wishlist_count,
    }
    return render(request,'header.html',context)

def footer_view(request):
    context = {
        'FooterOne':FooterOne.objects.all(),
        'SiteSetting':SiteSetting.objects.filter(active=True).last(),
    }
    return render(request,'footer.html',context)

@login_required(login_url='/')
def wishlist_view(request):
    wishlist = WishList.objects.filter(account__user=request.user)
    context = {
        'wishlist': wishlist
    }
    return render(request,'wishlist.html',context)

@login_required(login_url='/')
def wishlist_delete_item(request,id):
    wish_item = WishList.objects.get(id=id)
    wish_item.delete()
    messages.success(request,'محصول از علاقه مندی های شما حذف شد')
    return redirect('home:wishlist')

