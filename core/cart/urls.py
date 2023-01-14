from django.urls import path
from . import views

app_name='cart'

urlpatterns = [
    path('add_user_order/',views.add_user_order,name='add_user_order'),
    path('cart/',views.user_open_order,name='user_open_order'),
    path('removecookie/<id>/',views.remove_from_cookie,name='remove_from_cookie'),
]
