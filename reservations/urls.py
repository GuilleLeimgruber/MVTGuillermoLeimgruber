from django.urls import path

from reservations.views import list_reservations, create_reservation, update_reservation, ReservationsListView, \
    ReservationsCreateView, ReservationsUpdateView, ReservationsDeleteView




urlpatterns = [
    path('create-reservation/', ReservationsCreateView.as_view(), name = 'create_reservation'),
    path('list-reservations/', ReservationsListView.as_view(), name = 'list_providers'),
    path('update-reservation/<int:pk>/', ReservationsUpdateView.as_view(), name = 'update_reservation'),
    path('delete-reservation/<int:pk>/', ReservationsDeleteView.as_view(), name = 'delete_reservation'),
    
]