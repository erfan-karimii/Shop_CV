from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.

def index_view(request):
    return HttpResponse('<h1>product</h1>')



def listview(request):
    posts = Product.objects.filter(is_active=True).order_by('-created')
    paginator = Paginator(posts,20)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    context = {
        'posts':posts,
        'count' : Product.objects.filter(is_active=True).count(),
        # 'paginator':Paginator.object_list
        }
    return render(request,'listview.html',context)