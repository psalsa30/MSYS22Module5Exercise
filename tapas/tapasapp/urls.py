from django.urls import path
from . import views


urlpatterns = [
    path('basic_list', views.view_basic_list, name='view_basic_list'),
    path('', views.view_menu, name='view_menu'),
    path('add_menu', views.add_menu, name='add_menu'),
    path('view_wines', views.view_wines, name='view_wines'),
    path('view_large_dishes', views.view_large_dishes, name='view_large_dishes'),
    path('view_coursed_menus', views.view_coursed_menus, name='view_coursed_menus'),
    path('button', views.button, name='button')
]