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
    path('footer_two/', views.FooterTwoCreateView.as_view(),name='footer_zir'),
    path('delete/footertwo/<pk>',views.FooterTwoDeleteView.as_view(),name='footer_zir_delete'),
    
    #----------Start-----------Onsale---------------------
    path('on_sale/<pk>',views.OnSaleView.as_view(),name='on_sale'),

    #----------Start-----------sitesetting---------------------
    path('sitesetting/<pk>',views.SiteSettingView.as_view(),name='sitesetting'),

    #----------Start-----------Slider---------------------
    path('detail/slider/<pk>/',views.SliderView.as_view(),name='slider_detail'),
    path('slider/', views.SliderCreateView.as_view(),name='slider'),
    path('slider_list/', views.SliderListView.as_view(),name='slider_list'),
    path('delete/slider/<pk>',views.SliderDeleteView.as_view(),name='slider_delete'),

    #----------Start-----------Tabligh---------------------
    path('detail/tabligh/<pk>/',views.TablighView.as_view(),name='tabligh_detail'),
    path('tabligh/', views.TablighCreateView.as_view(),name='tabligh'),
    path('tabligh_list/', views.TablighListView.as_view(),name='tabligh_list'),
    path('delete/tabligh/<pk>',views.TablighDeleteView.as_view(),name='tabligh_delete'),
    
    #----------Start-----------aboutusgeneral---------------------
    path('aboutusgeneral/<pk>',views.AboutUsGeneralView.as_view(),name='aboutusgeneral'),

    #----------Start-----------AboutUsProgressBar---------------------
    path('detail/aboutus_progress_bar/<pk>/',views.AboutUsProgressBarView.as_view(),name='aboutus_progress_bar_detail'),
    path('aboutus_progress_bar/', views.AboutUsProgressBarCreateView.as_view(),name='aboutus_progress_bar'),
    path('aboutus_progress_bar_list/', views.AboutUsProgressBarListView.as_view(),name='aboutus_progress_bar_list'),
    path('delete/aboutus_progress_bar/<pk>',views.AboutUsProgressBarDeleteView.as_view(),name='aboutus_progress_bar_delete'),

    #----------Start-----------AboutUsProperty---------------------
    path('detail/aboutus_property/<pk>/',views.AboutUsPropertyView.as_view(),name='aboutus_property_detail'),
    path('aboutus_property/', views.AboutUsPropertyCreateView.as_view(),name='aboutus_property'),
    path('aboutus_property_list/', views.AboutUsPropertyListView.as_view(),name='aboutus_property_list'),
    path('delete/aboutus_property/<pk>',views.AboutUsPropertyDeleteView.as_view(),name='aboutus_property_delete'),


]
