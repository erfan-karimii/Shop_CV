from django.urls import path 
from .views import index_view , footer_view , header_view

app_name = 'home'

urlpatterns = [
    path('',index_view,name='home'),
    path('header/',header_view,name='header'),
    path('footer/',footer_view,name='footer'),

]
