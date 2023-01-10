from django.urls import path

from . import views

app_name = 'cms'

urlpatterns = [
    #-----------Start---------NavOne-----------------
    path('navone/',views.NavOneCreateView.as_view(),name='navone'),
    path('navonelist/',views.NavOneListView.as_view(),name='nav_list'),
    path('detail/navone/<pk>/',views.NavOneDetailView.as_view(),name='detail_navone'),
    path('delete/navone/<pk>/',views.NavOneDeleteView.as_view(),name='nav_delete'),

    #-----------Start---------NavTwo-----------------
    path('navtwo/',views.NavTwoCreateView.as_view(),name='navtwo'),
    path('detail/navtwo/<pk>/',views.NavTwoDetailView.as_view(),name='detail_navtwo'),
    path('delete/navtwo/<pk>/',views.NavTwoDeleteView.as_view(),name='navtwo_delete'),

    #---------Start-----------FooterOne------------------------
    path('footer_one/',views.FooterOneCreateView.as_view(),name='footer_asli'),
    path('footer_list/',views.FooterListView.as_view(),name='footer_list'),
    path('detail/footer_one/<pk>/',views.FooterDetailView.as_view(),name='footer_asli_detail'),
    path('delete/footer_one/<pk>/',views.FooterOneDeleteView.as_view(),name='footer_one_delete'),

    #----------Start-----------FooterTwo---------------------
    path('detail/footer_two/<pk>/',views.FooterZirDetailView.as_view(),name='footer_zir_detail'),
]
