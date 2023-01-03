from django.urls import path 
from .views import index_view,listview,detailview

app_name='product'

urlpatterns = [
    path('product/',index_view,name='home'),
    path('listview/',listview,name='listview'),
    path('det/<id>/',detailview,name='detailview'),
]
