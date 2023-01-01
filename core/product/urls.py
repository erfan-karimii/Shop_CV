from django.urls import path 
from .views import index_view


urlpatterns = [
    path('product/',index_view,name='home'),
]
