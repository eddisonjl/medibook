from django.db import models
from django.contrib.auth.models import User


class Specialty(models.Model):
    name = models.CharField(max_length=100, verbose_name="Especialidad")
    icon = models.CharField(max_length=50, default="fa-stethoscope", verbose_name="Ícono")

    class Meta:
        verbose_name = "Especialidad"
        verbose_name_plural = "Especialidades"

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='doctor_profile')
    specialty = models.ForeignKey(Specialty, on_delete=models.SET_NULL, null=True, related_name='doctors')
    license_number = models.CharField(max_length=50, unique=True, verbose_name="Número de Colegiado")
    phone = models.CharField(max_length=20, verbose_name="Teléfono")
    bio = models.TextField(blank=True, verbose_name="Biografía")
    avatar = models.ImageField(upload_to='doctors/', blank=True, null=True)
    consultation_fee = models.DecimalField(max_digits=8, decimal_places=2, default=0, verbose_name="Tarifa de consulta")

    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctores"

    def __str__(self):
        return f"Dr. {self.user.get_full_name()} - {self.specialty}"

    def get_full_name(self):
        return self.user.get_full_name()


class Patient(models.Model):
    BLOOD_TYPES = [
        ('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'),
        ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='patient_profile')
    date_of_birth = models.DateField(verbose_name="Fecha de nacimiento")
    phone = models.CharField(max_length=20, verbose_name="Teléfono")
    blood_type = models.CharField(max_length=3, choices=BLOOD_TYPES, blank=True, verbose_name="Tipo de sangre")
    address = models.TextField(blank=True, verbose_name="Dirección")
    emergency_contact = models.CharField(max_length=100, blank=True, verbose_name="Contacto de emergencia")
    emergency_phone = models.CharField(max_length=20, blank=True, verbose_name="Teléfono de emergencia")

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

    def __str__(self):
        return self.user.get_full_name()


class Appointment(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pendiente'),
        ('confirmed', 'Confirmada'),
        ('completed', 'Completada'),
        ('cancelled', 'Cancelada'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    date = models.DateField(verbose_name="Fecha")
    time = models.TimeField(verbose_name="Hora")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending', verbose_name="Estado")
    reason = models.TextField(verbose_name="Motivo de consulta")
    notes = models.TextField(blank=True, verbose_name="Notas del médico")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"
        ordering = ['-date', '-time']
        unique_together = ['doctor', 'date', 'time']

    def __str__(self):
        return f"Cita: {self.patient} con Dr. {self.doctor.get_full_name()} el {self.date}"

    def get_status_badge(self):
        badges = {
            'pending': 'warning',
            'confirmed': 'primary',
            'completed': 'success',
            'cancelled': 'danger',
        }
        return badges.get(self.status, 'secondary')
