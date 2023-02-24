from django.urls import path

from deliveries.views import list_deliveries, create_delivery, update_delivery, \
     DeliveriesListView, DeliveriesCreateView, DeliveriesDeleteView, DeliveriesUpdateView




urlpatterns = [
    path('create-delivery/', DeliveriesCreateView.as_view(), name = 'create_deliveriy'),
    path('list-deliveries/', DeliveriesListView.as_view(), name = 'list_deliveries'),
    path('update-delivery/<int:pk>/', DeliveriesUpdateView.as_view(), name = 'update_delivery'),
    path('delete-delivery/<int:pk>/', DeliveriesDeleteView.as_view(), name = 'delete_delivery'),
]