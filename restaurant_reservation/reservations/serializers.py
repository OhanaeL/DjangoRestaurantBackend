from rest_framework import serializers
from .models import Table, Reservation

class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = ['table_number', 'capacity', 'status']

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['user', 'table', 'date', 'time']

    def validate(self, data):
        # Check if the table is already reserved for the given date and time
        if Reservation.objects.filter(
            table=data['table'], 
            date=data['date'], 
            time=data['time']
        ).exists():
            raise serializers.ValidationError("This table is already reserved for the selected date and time.")
        return data
