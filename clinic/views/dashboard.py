from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db import models
from ..models import Patient, Professional, Payment, Appointment
from ..decorator import group_required

@login_required
def dashboard(request):
    today = timezone.now().date()
    start_of_month = today.replace(day=1)
    
    # Filter for expiring or expired plans
    all_payments = Payment.objects.all().order_by('payment_date')
    expiring_plans = [p for p in all_payments if p.status != 'active']
    
    # Separate counts
    expired_count = len([p for p in expiring_plans if p.status == 'expired'])
    warning_count = len([p for p in expiring_plans if p.status == 'warning'])
    
    # Permissions check
    is_admin = request.user.is_superuser or request.user.groups.filter(name='Administradores').exists()
    
    # Calculate revenue only for admins
    month_revenue = 0
    if is_admin:
        month_revenue = Payment.objects.filter(payment_date__gte=start_of_month).aggregate(models.Sum('amount'))['amount__sum'] or 0

    context = {
        'total_patients': Patient.objects.count(),
        'total_professionals': Professional.objects.count(),
        'today_appointments': Appointment.objects.filter(date__date=today).count(),
        'month_revenue': month_revenue,
        'upcoming_appointments': Appointment.objects.filter(date__date=today).order_by('date')[:10],
        'expiring_plans': expiring_plans[:5],
        'expired_count': expired_count,
        'warning_count': warning_count,
        'is_admin': is_admin,
    }
    return render(request, 'clinic/dashboard.html', context)

@group_required('Administradores','Profissionais')
def today(request):
    appointments_today = Appointment.objects.filter(date__date=timezone.now().date()).order_by('date')
    return render(request, 'clinic/today.html', {'appointments': appointments_today})

@group_required('Administradores','Profissionais')
def settings(request):
    return render(request, 'clinic/settings.html')

def denied(request):
    return render(request, 'clinic/denied.html')
