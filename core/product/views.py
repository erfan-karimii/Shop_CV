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
      
        }
    return render(request,'listview.html',context)


def detailview(request,id):
    post = get_object_or_404(Product,id=id)
    tag = []
    get_tag = post.tag.all()
    for x in get_tag:
        tag.append(x.name)
    context = {
        'post':post,
        'tags':tag,
    }
    return render(request,'detailview.html',context)
