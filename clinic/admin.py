from django.contrib import admin
from .models import Patient, Professional, HealthPlan, Payment, Appointment
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'cpf', 'phone', 'email')
    search_fields = ('name', 'cpf')

@admin.register(Professional)
class ProfessionalAdmin(admin.ModelAdmin):
    list_display = ('name', 'professional_type', 'registration_number', 'specialty')
    list_filter = ('professional_type',)
    search_fields = ('name', 'registration_number')

@admin.register(HealthPlan)
class HealthPlanAdmin(admin.ModelAdmin):
    list_display = ('title', 'validity_days')
    search_fields = ('title',)

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'plan', 'amount', 'payment_date', 'status')
    list_filter = ('payment_date', 'plan')
    search_fields = ('patient__name', 'notes')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date', 'weight', 'clinical_notes', 'prescription')
    list_filter = ('patient', 'date')
    date_hierarchy = 'date'

