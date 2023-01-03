from django.urls import path 
from .views import index_view,listview


urlpatterns = [
    path('product/',index_view,name='home'),
    path('listview/',listview,name='listview'),
]
