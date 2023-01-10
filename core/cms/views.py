from django.shortcuts import render,redirect
from django.views.generic import (
    CreateView, ListView  , UpdateView , View)
# Create your views here.
from home.models import NavOne,NavTwo,FooterOne,FooterTwo
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect

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
        return redirect("cms:nav_list")

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
