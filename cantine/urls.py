# urls.py
from django.urls import path
from .views.menu_view import menu_list, create_menu, menu_list, menu_detail, update_menu, delete_menu
from .views.plat_view import plat_list, plat_detail,create_plat, plat_list, plat_detail, update_plat, delete_plat


app_name = 'cantine'
urlpatterns = [
    
    #Routes pour Plats 
    path('plat/', plat_list, name='plat_list'),
    path('plat/<int:pk>/', plat_detail, name='plat_detail'),
    path('plat/new/', create_plat, name='create_plat'),
    path('plat/<int:pk>/edit/', update_plat, name='update_plat'),
    path('plat/<int:pk>/delete/', delete_plat, name='delete_plat'),
    
    
    #Routes pour Menus

    path('menu/', menu_list, name='menu_list'),
    path('menu/<int:pk>/', menu_detail, name='menu_detail'),
    path('menu/new/', create_menu, name='create_menu'),
    path('menu/<int:pk>/edit/', update_menu, name='update_menu'),
    path('menu/<int:pk>/delete/', delete_menu, name='delete_menu'),

]
