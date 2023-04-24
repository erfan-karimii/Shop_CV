from django.urls import path 
from .views import listview,detailview,SearchView

app_name='product'

urlpatterns = [
    path('listview/',listview,name='listview'),
    path('detail/<int:id>/',detailview,name='detailview'),
    path('search/',SearchView,name='SearchView')
]
