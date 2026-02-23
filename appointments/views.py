from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.utils import timezone
from .models import Appointment, Doctor, Patient, Specialty
from .forms import AppointmentForm, PatientProfileForm


def home(request):
    specialties = Specialty.objects.all()
    doctors = Doctor.objects.select_related('user', 'specialty').all()[:6]
    context = {
        'specialties': specialties,
        'doctors': doctors,
        'total_doctors': Doctor.objects.count(),
        'total_appointments': Appointment.objects.filter(status='completed').count(),
    }
    return render(request, 'appointments/home.html', context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        profile_form = PatientProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            patient = profile_form.save(commit=False)
            patient.user = user
            patient.save()
            login(request, user)
            messages.success(request, '¡Cuenta creada exitosamente!')
            return redirect('appointments:list')
    else:
        form = UserCreationForm()
        profile_form = PatientProfileForm()
    return render(request, 'registration/register.html', {'form': form, 'profile_form': profile_form})


@login_required
def appointment_list(request):
    try:
        patient = request.user.patient_profile
        appointments = patient.appointments.select_related('doctor__user', 'doctor__specialty').all()
    except Patient.DoesNotExist:
        appointments = []
    
    status_filter = request.GET.get('status', '')
    if status_filter:
        appointments = appointments.filter(status=status_filter)

    context = {
        'appointments': appointments,
        'status_filter': status_filter,
        'today': timezone.now().date(),
    }
    return render(request, 'appointments/list.html', context)


@login_required
def appointment_create(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.patient = request.user.patient_profile
            appointment.save()
            messages.success(request, '¡Cita agendada exitosamente!')
            return redirect('appointments:list')
    else:
        form = AppointmentForm()
    return render(request, 'appointments/create.html', {'form': form})


@login_required
def appointment_detail(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, patient=request.user.patient_profile)
    return render(request, 'appointments/detail.html', {'appointment': appointment})


@login_required
def appointment_cancel(request, pk):
    appointment = get_object_or_404(Appointment, pk=pk, patient=request.user.patient_profile)
    if appointment.status in ['pending', 'confirmed']:
        appointment.status = 'cancelled'
        appointment.save()
        messages.success(request, 'Cita cancelada.')
    return redirect('appointments:list')


def doctor_list(request):
    specialty_id = request.GET.get('specialty')
    doctors = Doctor.objects.select_related('user', 'specialty').all()
    if specialty_id:
        doctors = doctors.filter(specialty_id=specialty_id)
    specialties = Specialty.objects.all()
    return render(request, 'appointments/doctors.html', {'doctors': doctors, 'specialties': specialties})
