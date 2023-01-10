from django.urls import path

from . import views

app_name = 'cms'

urlpatterns = [
    path('navone/',views.NavOneCreateView.as_view(),name='navone'),
    path('navonelist/',views.NavOneListView.as_view(),name='nav_list'),
    path('detail/navone/<pk>/',views.NavOneDetailView.as_view(),name='detail_navone'),
    path('delete/navone/<pk>/',views.NavOneDeleteView.as_view(),name='nav_delete'),
]
