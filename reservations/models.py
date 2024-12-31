from django.db import models
from django.contrib.auth.models import User  # Import User model

# Table Model
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    status = models.CharField(max_length=10, choices=[('Available', 'Available'), ('Reserved', 'Reserved')], default='Available')

    def __str__(self):
        return f"Table {self.table_number}"

# Reservation Model
class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reservations')
    table = models.ForeignKey(Table, on_delete=models.CASCADE, related_name='reservations')
    date = models.DateField()
    time = models.TimeField()
    
    def __str__(self):
        return f"Reservation for {self.user.username} on {self.date} at {self.time}"
