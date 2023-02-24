from django.urls import path

from providers.views import list_providers, create_provider, update_provider, delete_provider, \
     ProvidersListView, ProvidersCreateView, ProvidersDeleteView, ProvidersUpdateView




urlpatterns = [
    path('list-providers/', ProvidersListView.as_view(), name = 'list_providers'),
    path('create-provider/', ProvidersCreateView.as_view(), name = 'create_provider'),
    path('delete-provider/<int:pk>/', ProvidersDeleteView.as_view(), name = 'delete_provider'),
    path('update-provider/<int:pk>/', ProvidersUpdateView.as_view(), name = 'update_provider'),
    
]