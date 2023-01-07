from django.urls import path 
from .views import listview,detailview

app_name='product'

urlpatterns = [
    path('listview/',listview,name='listview'),
    path('detail/<id>/',detailview,name='detailview'),
]
