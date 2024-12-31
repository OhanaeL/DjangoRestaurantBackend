from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Table, Reservation
from .serializers import TableSerializer, ReservationSerializer
from django.db import transaction

@api_view(['GET'])
def available_tables(request):
    tables = Table.objects.filter(status='Available')
    serializer = TableSerializer(tables, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_reservation(request, id):
    # Retrieve the reservation by the provided ID
    reservation = get_object_or_404(Reservation, id=id)
    
    # Example response, you can customize this based on your model
    data = {
        "table": reservation.table.table_number,
        "date": reservation.date,
        "time": reservation.time,
        "user": reservation.user.username,
    }
    
    return Response(data)

@api_view(['POST'])
def create_reservation(request):
    serializer = ReservationSerializer(data=request.data)
    if serializer.is_valid():
        reservation = serializer.save()
        reservation.table.status = 'Reserved'
        reservation.table.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT', 'PATCH'])
def manage_reservation(request, id):
    reservation = get_object_or_404(Reservation, id=id)
    
    if request.method == 'PUT':
        # Update the entire reservation
        serializer = ReservationSerializer(reservation, data=request.data)
    elif request.method == 'PATCH':
        # Partially update the reservation (optional fields only)
        serializer = ReservationSerializer(reservation, data=request.data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=400)