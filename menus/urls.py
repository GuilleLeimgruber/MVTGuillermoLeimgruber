from django.urls import path

from menus.views import list_menus, create_menu, create_category, list_categories, update_menu, \
     MenusCreateView, MenusDeleteView, MenusUpdateView 




urlpatterns = [
    path('create-menu/', MenusCreateView.as_view(), name = 'create_menu'),
    path('list-menus/',list_menus, name =  'list_menus'),
    path('create-category/', create_category),
    path('list-categories/', list_categories),
    path('update-menu/<int:pk>/', MenusUpdateView.as_view(), name = 'update_menu'),
    path('delete-menu/<int:pk>/', MenusDeleteView.as_view(), name = 'delete_menu')
]