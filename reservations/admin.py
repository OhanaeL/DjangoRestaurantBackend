from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Table, Reservation
from django import forms

# Customize the User Admin to display the 'id' field
class CustomUserAdmin(UserAdmin):
    list_display = ('id', 'username', 'email', 'first_name', 'last_name', 'is_active')  # Add 'id' to the list
    search_fields = ('username', 'email')

# Register the customized User Admin
admin.site.unregister(User)  # Unregister the original User admin
admin.site.register(User, CustomUserAdmin)  # Register the customized User admin

class ReservationAdminForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = '__all__'

class ReservationAdmin(admin.ModelAdmin):
    form = ReservationAdminForm

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Table)
