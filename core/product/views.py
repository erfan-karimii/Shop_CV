from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Product
# Create your views here.

def index_view(request):
    return HttpResponse('<h1>product</h1>')



def listview(request):
    posts = Product.objects.filter(is_active=True).order_by('-created')
    paginator = Paginator(posts,2)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {
        'posts':posts,
        'count' : Product.objects.filter(is_active=True).count(),
        # 'listobj' : posts.object_list.count()
        }
    return render(request,'listview.html',context)


def detailview(request,id):
    post = get_object_or_404(Product,id=id)
    # print(post.tag.all())
    my_posts = []
    for x in post.tag.all():
        for m in x.product_set.all():
            if m in my_posts:
                continue
            my_posts.append(m)
    print(my_posts)

        
    context = {
        'post':post,
        'my_posts':my_posts
    }
    return render(request,'detailview.html',context)
