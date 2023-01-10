from django.shortcuts import render,redirect
from django.views.generic import (
    CreateView, ListView  , UpdateView , View)
# Create your views here.
from home.models import NavOne
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