from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Product,GalleryImage,Comment
from django.db.models import Count ,Avg
from .forms import CommentForm
from django.contrib import messages

# Create your views here.



def listview(request):
    number = 2
    if request.GET.get('show-number'):
        number = request.GET.get('show-number')
    posts = Product.objects.filter(is_active=True).order_by('-created')
    paginator = Paginator(posts,number)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {
        'posts':posts,
        'count' : Product.objects.filter(is_active=True).count(),
        'number' : number,
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
            print(comment_form.errors)
    else:
        comment_form = CommentForm()
    ids=post.tag.values_list('id',flat=True)
    products = Product.objects.filter(tag__in=ids).exclude(id=id)
    products = products.annotate(s_count=Count('tag')).order_by('-s_count','-created')[:6]
    
    context = {
        'post':post,
        'my_posts':products,
        'comment':comments,
        'comment_form':comment_form,
    }
    return render(request,'detailview.html',context)

