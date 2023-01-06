from django.core.paginator import Paginator
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Product,GalleryImage,Comment
from django.db.models import Count
from .forms import CommentForm
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
    print(post.id)
    comments = Comment.objects.filter(is_show=True,product_id=id)

    if request.method == "POST":
        print("sd")
        comment_form = CommentForm(request.POST)
        print(comment_form.errors)
        if comment_form.is_valid():
            print("as")
            comment_form.save()
    else:
        comment_form = CommentForm()
    ids=post.tag.values_list('id',flat=True)
    products = Product.objects.filter(tag__in=ids).exclude(id=id)
    products = products.annotate(s_count =Count('tag')).order_by('-s_count','-updated')[:6]
    
    context = {
        'post':post,
        'my_posts':products,
        'comment':comments,
        'comment_form':comment_form,
    }
    return render(request,'detailview.html',context)

