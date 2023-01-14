from django.shortcuts import render,redirect , get_object_or_404
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from django.urls import reverse_lazy
from django.db.models import ProtectedError
import datetime
from django.views.generic import (
    CreateView, ListView  , UpdateView , View,TemplateView)
from home.models import NavOne,NavTwo,FooterOne,FooterTwo,OnSale,SiteSetting,Slider,Tabligh
from aboutus.models import AboutUsGeneral , AboutUsProgressBar , AboutUsProperty
from contactus.models import Newsletter , ContactUsKeeper 
from product.models import Product,Category,Comment,Color,GalleryImage,Size,TagProduct
from .forms import ProductForm , ColorForm , SizeForm , GalleryImageForm
from account.models import Profile,User
# Create your views here.

#-----------Start---------NavOne-----------------
class NavOneCreateView(CreateView):
    model = NavOne
    fields = "__all__"
    template_name = 'cms/nav/nav_one.html'
    success_url = reverse_lazy("cms:nav_list")

    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ثبت شد')
        return super().form_valid(form)

class NavOneListView(ListView):
    model = NavOne
    template_name = 'cms/nav/nav_list.html'
    context_object_name = 'navsone'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['navstwo'] =NavTwo.objects.all()
        return context

class NavOneDetailView(UpdateView):
    model = NavOne
    template_name = 'cms/nav/nav_one_detail.html'
    context_object_name = 'navone'
    fields="__all__"
    success_url = reverse_lazy("cms:nav_list")
    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ویرایش شد')
        return super().form_valid(form)

class NavOneDeleteView(View):
    def get(self, request, *args, **kwargs):
        NavOne.objects.get(id=kwargs['pk']).delete()
        messages.success(self.request,'با موفقیت حذف شد')
        return redirect("cms:nav_list")

#-------------End-------NavOne-----------------



#-----------Start---------NavTwo-----------------
class NavTwoCreateView(CreateView):
    model = NavTwo
    fields = "__all__"
    template_name = 'cms/nav/nav_Two.html'
    success_url = reverse_lazy("cms:nav_list")

    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ثبت شد')
        return super().form_valid(form)

class NavTwoDetailView(UpdateView):
    model = NavTwo
    template_name = 'cms/nav/nav_two_detail.html'
    context_object_name = 'navtwo'
    fields="__all__"
    success_url = reverse_lazy("cms:nav_list")
    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ویرایش شد')
        return super().form_valid(form)

class NavTwoDeleteView(View):
    def get(self, request, *args, **kwargs):
        NavTwo.objects.get(id=kwargs['pk']).delete()
        messages.success(self.request,'با موفقیت حذف شد')
        return redirect("cms:nav_list")
#-------------End-------NavTwo-----------------


#--------------Start----------Footer--------------
class FooterOneCreateView(CreateView):
    model = FooterOne
    fields = "__all__"
    template_name = 'cms/footer/footer_asli.html'
    success_url = reverse_lazy("cms:footer_list")

    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ثبت شد')
        return super().form_valid(form)

class FooterListView(ListView):
    model = FooterOne
    template_name = 'cms/footer/footer_list.html'
    context_object_name = 'footers'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['footer_zir'] =FooterTwo.objects.all()
        return context

class FooterDetailView(UpdateView):
    model = FooterOne
    template_name = 'cms/footer/footer_asli_detail.html'
    context_object_name = 'footerasil'
    fields="__all__"
    success_url = reverse_lazy("cms:footer_list")
    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ویرایش شد')
        return super().form_valid(form)

class FooterOneDeleteView(View):
    def get(self, request, *args, **kwargs):
        FooterOne.objects.get(id=kwargs['pk']).delete()
        messages.success(self.request,'با موفقیت حذف شد')
        return redirect("cms:footer_list")

#--------------End----------Footer--------------


#--------------Start----------Footer_zir--------------
class FooterZirDetailView(UpdateView):
    model = FooterTwo
    template_name = 'cms/footer/footer_zir_detail.html'
    context_object_name = 'footer_zir'
    fields="__all__"
    success_url = reverse_lazy("cms:footer_list")
    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ویرایش شد')
        return super().form_valid(form)

class FooterTwoCreateView(CreateView):
    model = FooterTwo
    fields = "__all__"
    template_name = 'cms/footer/footer_zir.html'
    success_url = reverse_lazy("cms:footer_list")

    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ثبت شد')
        return super().form_valid(form)

class FooterTwoDeleteView(View):
    def get(self, request, *args, **kwargs):
        FooterTwo.objects.get(id=kwargs['pk']).delete()
        messages.success(self.request,'با موفقیت حذف شد')
        return redirect("cms:footer_list")
#--------------Start----------Footer_zir--------------

#--------------Start----------on_sales--------------
class OnSaleView(UpdateView):
    model = OnSale
    template_name = 'cms/on_sale.html'
    fields="__all__"
    success_url = reverse_lazy("cms:on_sale", kwargs={'pk': 1})
    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ویرایش شد')
        return super().form_valid(form)
#--------------End----------on_sales--------------

#--------------Start----------sitesetting--------------
class SiteSettingView(UpdateView):
    model = SiteSetting
    template_name = 'cms/site_setting_edit.html'
    fields="__all__"
    success_url = reverse_lazy("cms:sitesetting", kwargs={'pk': 1})
    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ویرایش شد')
        return super().form_valid(form)
#--------------End----------sitesetting--------------

#--------------Start----------Slider--------------
class SliderListView(ListView):
    model = Slider
    template_name = 'cms/slider/slider_list.html'
    context_object_name = 'slider_list'

class SliderView(UpdateView):
    model = Slider
    template_name = 'cms/slider/slider_detail.html'
    context_object_name = 'slider'
    fields="__all__"
    success_url = reverse_lazy("cms:slider_list")
    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ویرایش شد')
        return super().form_valid(form)

class SliderCreateView(CreateView):
    model = Slider
    fields = "__all__"
    template_name = 'cms/slider/add_slider.html'
    success_url = reverse_lazy("cms:slider_list")

    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ثبت شد')
        return super().form_valid(form)

class SliderDeleteView(View):
    def get(self, request, *args, **kwargs):
        Slider.objects.get(id=kwargs['pk']).delete()
        messages.success(self.request,'با موفقیت حذف شد')
        return redirect("cms:slider_list")
#--------------Start----------Slider--------------

#--------------Start----------Tabligh--------------
class TablighListView(ListView):
    model = Tabligh
    template_name = 'cms/tabligh/tabligh_list.html'
    context_object_name = 'tabligh_list'

class TablighView(UpdateView):
    model = Tabligh
    template_name = 'cms/tabligh/tabligh_detail.html'
    context_object_name = 'tabligh'
    fields="__all__"
    success_url = reverse_lazy("cms:tabligh_list")
    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ویرایش شد')
        return super().form_valid(form)

class TablighCreateView(CreateView):
    model = Tabligh
    fields = "__all__"
    template_name = 'cms/tabligh/add_tabligh.html'
    success_url = reverse_lazy("cms:tabligh_list")

    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ثبت شد')
        return super().form_valid(form)

class TablighDeleteView(View):
    def get(self, request, *args, **kwargs):
        Tabligh.objects.get(id=kwargs['pk']).delete()
        messages.success(self.request,'با موفقیت حذف شد')
        return redirect("cms:tabligh_list")
#--------------Start----------Tabligh--------------

#--------------Start----------aboutusgeneral--------------
class AboutUsGeneralView(UpdateView):
    model = AboutUsGeneral
    template_name = 'cms/abous_us_general.html'
    fields="__all__"
    success_url = reverse_lazy("cms:aboutusgeneral", kwargs={'pk': 1})
    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ویرایش شد')
        return super().form_valid(form)
#--------------End----------aboutusgeneral--------------

#--------------Start----------AboutUsProgressBar--------------
class AboutUsProgressBarListView(ListView):
    model = AboutUsProgressBar
    template_name = 'cms/about_us/aboutus_progress_bar_list.html'
    context_object_name = 'aboutus_progress_bar_list'

class AboutUsProgressBarView(UpdateView):
    model = AboutUsProgressBar
    template_name = 'cms/about_us/aboutus_progress_bar_detail.html'
    context_object_name = 'aboutus_progress_bar'
    fields="__all__"
    success_url = reverse_lazy("cms:aboutus_progress_bar_list")
    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ویرایش شد')
        return super().form_valid(form)

class AboutUsProgressBarCreateView(CreateView):
    model = AboutUsProgressBar
    fields = "__all__"
    template_name = 'cms/about_us/add_aboutus_progress_bar.html'
    success_url = reverse_lazy("cms:aboutus_progress_bar_list")

    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ثبت شد')
        return super().form_valid(form)

class AboutUsProgressBarDeleteView(View):
    def get(self, request, *args, **kwargs):
        AboutUsProgressBar.objects.get(id=kwargs['pk']).delete()
        messages.success(self.request,'با موفقیت حذف شد')
        return redirect("cms:aboutus_progress_bar_list")

#--------------End----------AboutUsProgressBar--------------

#--------------Start----------AboutUsProperty--------------
class AboutUsPropertyListView(ListView):
    model = AboutUsProperty
    template_name = 'cms/about_us/aboutus_property_list.html'
    context_object_name = 'aboutus_property_list'

class AboutUsPropertyView(UpdateView):
    model = AboutUsProperty
    template_name = 'cms/about_us/aboutus_property_detail.html'
    context_object_name = 'aboutus_property'
    fields="__all__"
    success_url = reverse_lazy("cms:aboutus_property_list")
    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ویرایش شد')
        return super().form_valid(form)

class AboutUsPropertyCreateView(CreateView):
    model = AboutUsProperty
    fields = "__all__"
    template_name = 'cms/about_us/add_aboutus_property.html'
    success_url = reverse_lazy("cms:aboutus_property_list")

    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ثبت شد')
        return super().form_valid(form)

class AboutUsPropertyDeleteView(View):
    def get(self, request, *args, **kwargs):
        AboutUsProperty.objects.get(id=kwargs['pk']).delete()
        messages.success(self.request,'با موفقیت حذف شد')
        return redirect("cms:aboutus_property_list")
#--------------End----------AboutUsProperty--------------

#--------------Start----------Newsletter--------------
class NewsletterListView(ListView):
    model = Newsletter
    template_name = 'cms/newsletter/newsletter_list.html'
    context_object_name = 'newsletter_list'

class NewsletterView(UpdateView):
    model = Newsletter
    template_name = 'cms/newsletter/newsletter_detail.html'
    context_object_name = 'newsletter'
    fields="__all__"
    success_url = reverse_lazy("cms:newsletter_list")
    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ویرایش شد')
        return super().form_valid(form)

class NewsletterCreateView(CreateView):
    model = Newsletter
    fields = "__all__"
    template_name = 'cms/newsletter/add_newsletter.html'
    success_url = reverse_lazy("cms:newsletter_list")

    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ثبت شد')
        return super().form_valid(form)

class NewsletterDeleteView(View):
    def get(self, request, *args, **kwargs):
        Newsletter.objects.get(id=kwargs['pk']).delete()
        messages.success(self.request,'با موفقیت حذف شد')
        return redirect("cms:newsletter_list")
#--------------End----------Newsletter--------------

#--------------Start----------ContactUs--------------
class ContactUsListView(ListView):
    model = ContactUsKeeper
    template_name = 'cms/contactus/contactus_list.html'
    context_object_name = 'contactus_list'

class ContactUsView(UpdateView):
    model = ContactUsKeeper
    template_name = 'cms/contactus/contactus_detail.html'
    context_object_name = 'contactus'
    fields="__all__"
    success_url = reverse_lazy("cms:contactus_list")
    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ویرایش شد')
        return super().form_valid(form)

class ContactUsDeleteView(View):
    def get(self, request, *args, **kwargs):
        ContactUsKeeper.objects.get(id=kwargs['pk']).delete()
        messages.success(self.request,'با موفقیت حذف شد')
        return redirect("cms:contactus_list")
#--------------End----------ContactUs--------------

# START----------------PRODUCT------------------

class ProductList(ListView):
    model = Product
    template_name = 'cms/product/product_list.html'
    context_object_name = 'products'

class ProductView(TemplateView):
    template_name = 'cms/product/product_view.html'

    def post(self, request, *args, **kwargs):
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'محصول جدید با موفقیت اضافه شد')
            return redirect('cms:product_list')
        else:
            messages.error(request, 'مشکلی پیش امده است لطفا دوباره امتحان کنید.' )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ProductForm()
        return context 

class ProductDetail(TemplateView):
    template_name = 'cms/product/product_detail.html'
    def post(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs['id'])
        form = ProductForm(request.POST,request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
            return redirect('cms:product_list')
        else:
            print(form.errors)
            messages.error(request, 'مشکلی پیش امده است لطفا دوباره امتحان کنید.' )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = get_object_or_404(Product, id=kwargs['id'])
        context['form'] = ProductForm(instance=product)
        context['product'] = product
        context['size_form'] = SizeForm()
        context['color_form'] = ColorForm()
        context['image_form'] = GalleryImageForm()

        return context 

class ProductDelete(View):
    def get(self, request, *args, **kwargs):
        product = get_object_or_404(Product, id=kwargs['id'])
        try:
            product.delete()
            messages.success(request, 'محصول شما با موفقیت حذف شد')
        except ProtectedError:
            messages.error(request, 'لطفا قبل از حذف محصول عکس ها , رنگ ها و سایز های اضافی ان را حذف کنید' ) 
            return redirect('cms:product_detail',id=kwargs['id'])
        except Exception as e:
            messages.error(request, 'مشکلی پیش امده است لطفا دوباره امتحان کنید.' )     
        return redirect('cms:product_list')

class ProductAddSize(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        product.size_set.all().delete()
        
        size_deleted_list = request.POST.getlist('is_delete')
        size_name_list = request.POST.getlist('size')
        size_ekhtelaf_list = request.POST.getlist('Ekhtelaf')
        size_list = zip(size_name_list,size_ekhtelaf_list)
        
        Size.objects.bulk_create([
            Size(product=product,size=size[0],Ekhtelaf=size[1])\
            for size in size_list\
            if size[0] not in size_deleted_list 
            ])
        
        messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
        return redirect('cms:product_detail',id=product_id)

class ProductAddColor(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        product.color_set.all().delete()
        
        color_deleted_list = request.POST.getlist('is_delete')
        color_name_list = request.POST.getlist('color')
        color_ekhtelaf_list = request.POST.getlist('Ekhtelaf')
        color_list = zip(color_name_list,color_ekhtelaf_list)
    
        Color.objects.bulk_create([
            Color(product=product,color=color[0],Ekhtelaf=color[1])\
            for color in color_list\
            if color[0] not in color_deleted_list 
            ])

        
        messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
        return redirect('cms:product_detail',id=product_id)

class ProductAddImage(View):
    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        product = Product.objects.get(id=product_id)
        
        image_deleted_list = request.POST.getlist('is_delete')
        image_name_list = request.FILES.getlist('image')
        image_alt_list = request.POST.getlist('alt')
        image_list = zip(image_name_list,image_alt_list)
        
        # delete checkmarked images
        for image in image_deleted_list:
            GalleryImage.objects.filter(image=image).delete()  
        
        #create new image
        x = GalleryImage.objects.bulk_create([
            GalleryImage(product=product,image=image[0],alt=image[1]) \
        for image in image_list
            ])
        # save thumnail for new images
        if x:
            x[0].save()

           
        messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
        return redirect('cms:product_detail',id=product_id)

class ProductCahngeAltAjax(View):
    def get(self, request, *args, **kwargs):
        img = request.GET.get('img')
        alt = request.GET.get('val')
        id = request.GET.get('id')
        product = Product.objects.get(id = id)
        product.galleryimage_set.filter(image=img).update(alt=alt)
        messages.success(request, 'تغییرات شما با موفقیت اعمال شد')
        return JsonResponse({})

def search_name(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        products = Product.objects.filter(name__icontains=name)
    context = {
        'products': products,
    }
    return render(request, 'cms/product/product_list.html', context) 


# END----------------PRODUCT------------------

#--------------Start----------Category--------------
class CategoryListView(ListView):
    model = Category
    template_name = 'cms/category/category_list.html'
    context_object_name = 'category_list'

class CategoryView(UpdateView):
    model = Category
    template_name = 'cms/category/category_detail.html'
    context_object_name = 'category'
    fields="__all__"
    success_url = reverse_lazy("cms:category_list")
    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ویرایش شد')
        return super().form_valid(form)

class CategoryCreateView(CreateView):
    model = Category
    fields = "__all__"
    template_name = 'cms/category/add_category.html'
    success_url = reverse_lazy("cms:category_list")

    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ثبت شد')
        return super().form_valid(form)

class CategoryDeleteView(View):
    def get(self, request, *args, **kwargs):
        Category.objects.get(id=kwargs['pk']).delete()
        messages.success(self.request,'با موفقیت حذف شد')
        return redirect("cms:category_list")
#--------------End----------Category--------------

#--------------Start----------TagProduct--------------
class TagProductListView(ListView):
    model = TagProduct
    template_name = 'cms/tag/tag_list.html'
    context_object_name = 'tag_list'

class TagProductView(UpdateView):
    model = TagProduct
    template_name = 'cms/tag/tag_detail.html'
    context_object_name = 'tag'
    fields="__all__"
    success_url = reverse_lazy("cms:tag_list")
    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ویرایش شد')
        return super().form_valid(form)

class TagProductCreateView(CreateView):
    model = TagProduct
    fields = "__all__"
    template_name = 'cms/tag/add_tag.html'
    success_url = reverse_lazy("cms:tag_list")

    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ثبت شد')
        return super().form_valid(form)

class TagProductDeleteView(View):
    def get(self, request, *args, **kwargs):
        TagProduct.objects.get(id=kwargs['pk']).delete()
        messages.success(self.request,'با موفقیت حذف شد')
        return redirect("cms:tag_list")
#--------------End----------TagProduct--------------

#--------------Start----------Comment--------------
class CommentListView(ListView):
    model = Comment
    template_name = 'cms/comment/comment_list.html'
    context_object_name = 'comment_list'

class CommentView(UpdateView):
    model = Comment
    template_name = 'cms/comment/comment_detail.html'
    context_object_name = 'comment'
    fields="__all__"
    success_url = reverse_lazy("cms:comment_list")
    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ویرایش شد')
        return super().form_valid(form)


class CommentDeleteView(View):
    def get(self, request, *args, **kwargs):
        Comment.objects.get(id=kwargs['pk']).delete()
        messages.success(self.request,'با موفقیت حذف شد')
        return redirect("cms:comment_list")
#--------------End----------Comment--------------

#-------------Start---------Profile----------------

class ProfileListView(ListView):
    model = Profile
    template_name = 'cms/user/ProfleList.html'
    context_object_name = 'users'


class ProfileView(UpdateView):
    model = Profile
    template_name = 'cms/user/detailprofile.html'
    context_object_name = 'prof'
    fields="__all__"
    success_url = reverse_lazy("cms:ProfileListView")
    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ویرایش شد')
        return super().form_valid(form)
#--------------End---------Profile--------------------

#------------Start-----------User-------------------

class UserListView(ListView):
    model = User
    template_name = 'cms/user/user_list.html'
    context_object_name = 'user_list'

class UserCreateView(CreateView):
    model = User
    fields = "__all__"
    template_name = 'cms/user/add_user.html'
    success_url = reverse_lazy("cms:UserListView")

    def form_valid(self,form):
        password = form.cleaned_data['password']
        password = make_password(password)
        user = form.save(commit=False)
        user.password = password
        user.save()

        messages.success(self.request,'با موفقیت ثبت شد')
        return super().form_valid(form)
    
    def form_invalid(self,form):
        print(form.errors)
        return super().form_invalid(form)

        messages.success(self.request,'با موفقیت ثبت شد')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['now'] =datetime.datetime.now().strftime("%Y-%m-%d"+"T"+"%H:%M"),
        return context

class UserDetailView(UpdateView):
    model = User
    template_name = 'cms/user/detail_user.html'
    context_object_name = 'user'
    fields="__all__"
    success_url = reverse_lazy("cms:UserListView")
    def form_valid(self,form):
        messages.success(self.request,'با موفقیت ویرایش شد')
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in the publisher
        context['now'] =datetime.datetime.now().strftime("%Y-%m-%d"+"T"+"%H:%M"),
        return context

class UserDeleteView(View):
    def get(self, request, *args, **kwargs):
        User.objects.get(id=kwargs['pk']).delete()
        messages.success(self.request,'با موفقیت حذف شد')
        return redirect("cms:UserListView")
#------------End-----------User-------------------