from django.urls import path 
from .views import about_us_view

app_name='aboutus'

urlpatterns = [
    path('about-us/',about_us_view,name='about-us'),
]
