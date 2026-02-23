from django.contrib import admin
from .models import Specialty, Doctor, Patient, Appointment


@admin.register(Specialty)
class SpecialtyAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon']
    search_fields = ['name']


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', 'specialty', 'license_number', 'phone']
    list_filter = ['specialty']
    search_fields = ['user__first_name', 'user__last_name', 'license_number']

    def get_full_name(self, obj):
        return obj.get_full_name()
    get_full_name.short_description = 'Nombre'


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'phone', 'blood_type', 'date_of_birth']
    search_fields = ['user__first_name', 'user__last_name']


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['patient', 'doctor', 'date', 'time', 'status']
    list_filter = ['status', 'date', 'doctor__specialty']
    search_fields = ['patient__user__first_name', 'doctor__user__last_name']
    date_hierarchy = 'date'
