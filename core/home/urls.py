from django.urls import path 
from .views import index_view , footer_view , header_view , wishlist_view, add_to_wishlist ,\
                   wishlist_delete_item , quick_view,compare_view ,compare_view_2 ,compare_view_3,\
                   compare_listview ,add_to_wishlist_ajax

app_name = 'home'

urlpatterns = [
    path('',index_view,name='home'),
    path('header/',header_view,name='header'),
    path('footer/',footer_view,name='footer'),
    path('quick/<id>',quick_view,name='quick'),
    path('wishlist/',wishlist_view,name='wishlist'),
    path('wishlist-add/<user>/<product_id>/<color>/<size>/',add_to_wishlist,name='wishlist-add'),
    path('wishlist-add-ajax/<user>/<product_id>/<color>/<size>/',add_to_wishlist_ajax,name='wishlist-add-ajax'),
    path('wishlist_delete_item/<id>',wishlist_delete_item,name='wishlist_delete_item'),
    path('compare/',compare_view,name='compare'),
    path('compare_listview/<cat>/<id_1>',compare_listview,name='compare_listview'),
    path('compare/<id>',compare_view_2,name='compare_2'),
    path('compare/<id_1>/<id_2>',compare_view_3,name='compare_3'),



]
