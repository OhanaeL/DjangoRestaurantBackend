from django.urls import path
from .views import available_tables, create_reservation, get_reservation, manage_reservation  # Import the correct view from reservations

urlpatterns = [
    path('api/tables/available/', available_tables, name='available_tables'),
    path('api/reservations/create/', create_reservation, name='create_reservation'),
    path('api/reservations/<int:id>', get_reservation, name='get_reservation'),
    path('api/reservations/manage/<int:id>', manage_reservation, name='manage_reservation'),
]