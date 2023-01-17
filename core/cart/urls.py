from django.urls import path
from . import views

app_name='cart'

urlpatterns = [
    path('add_user_order/',views.add_user_order,name='add_user_order'),
    path('cart/',views.user_open_order,name='user_open_order'),
    path('removecookie/<id>/',views.remove_from_cookie,name='remove_from_cookie'),
    path('update_cart/',views.update_In_open_order,name='update_In_open_order'),
    path('get_order_id/',views.get_order_id,name='get_order_id'),
    path('check_out/',views.check_out_view,name='check_out'),
    path('how_user_pay/',views.how_user_pay,name='how_user_pay'),
    path('open_old_cart/',views.open_old_cart,name='open_old_cart'),

    # path('pay_by_cash/',views.pay_by_cash,name='pay_by_cash'),



]
