from django import forms
from .models import Appointment, Patient
from django.utils import timezone


class AppointmentForm(forms.ModelForm):
    date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min': str(timezone.now().date())}),
        label="Fecha"
    )
    time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type': 'time'}),
        label="Hora"
    )

    class Meta:
        model = Appointment
        fields = ['doctor', 'date', 'time', 'reason']
        widgets = {
            'reason': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Describa el motivo de su consulta...'}),
        }
        labels = {
            'doctor': 'Doctor',
            'reason': 'Motivo de consulta',
        }


class PatientProfileForm(forms.ModelForm):
    date_of_birth = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label="Fecha de nacimiento"
    )

    class Meta:
        model = Patient
        fields = ['date_of_birth', 'phone', 'blood_type', 'address']
        labels = {
            'phone': 'Teléfono',
            'blood_type': 'Tipo de sangre',
            'address': 'Dirección',
        }
