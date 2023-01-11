from django.shortcuts import render,redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView, ListView  , UpdateView , View)
from home.models import NavOne,NavTwo,FooterOne,FooterTwo,OnSale,SiteSetting,Slider,Tabligh
from aboutus.models import AboutUsGeneral , AboutUsProgressBar , AboutUsProperty
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