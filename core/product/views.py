from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Product,Comment 
from django.db.models import Count
from .forms import CommentForm
from django.contrib import messages

# Create your views here.

def listview(request):
    number = '2'
    if request.GET.get('show-number') and request.GET.get('show-number').isdigit():
        number = request.GET.get('show-number')
    option_value = '-created'
    if request.GET.get('orderby') and request.GET.get('orderby') in ('price','-price','-created'):
        option_value = request.GET.get('orderby')
    posts = Product.objects.filter(is_active=True).order_by('-instock',option_value)
    count = posts.count()
    paginator = Paginator(posts,number)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {
        'posts':posts,
        'count' : count,
        'number' : number,
        'op':option_value,
    }
    return render(request,'listview.html',context)

def detailview(request,id):        
    post = get_object_or_404(Product,id=id)
    comments = Comment.objects.filter(is_show=True,product_id=id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            messages.success(request,'پیام شما با موفقیت ثبت شد . با تایید ادمین نمایش داده میشود')
        else:
            messages.error(request,'متاسفانه مشکلی پیش امده است , لطفا دوباره امتحان کنید.')
    else:
        comment_form = CommentForm()
    ids=post.tag.values_list('id',flat=True)
    products = Product.objects.filter(tag__in=ids,instock=True).exclude(id=id)
    products = products.annotate(s_count=Count('tag')).order_by('-s_count','-created')[:6]
    
    context = {
        'post':post,
        'my_posts':products,
        'comment':comments,
        'comment_form':comment_form,
    }
    return render(request,'detailview.html',context)

def SearchView(request):

    search = request.GET.get('search','')
    category = request.GET.get('category')
    if category == '':
        products=Product.objects.filter(name__icontains=search).order_by('-instock','-created')
    else:
        products=Product.objects.filter(name__icontains=search,category=category).order_by('-instock','-created')
    

    context = {
        'posts':products
    }
    return render(request,'search_listview.html',context)