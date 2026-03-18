from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from .base import CrudMixin
from ..decorator import group_required
from ..models import Patient, Appointment, Payment

@group_required('Administradores','Profissionais','Financeiro')
class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'clinic/patient_list.html'
    context_object_name = 'patients'
    paginate_by = 6

    def get_queryset(self):
        qs = Patient.objects.all().order_by('first_name', 'last_name')
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(models.Q(first_name__icontains=q) | models.Q(last_name__icontains=q))
        return qs.order_by('first_name', 'last_name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_q'] = self.request.GET.get('q', '')
        return context

@group_required('Administradores','Profissionais','Financeiro')
class PatientCreateView(LoginRequiredMixin, CrudMixin, CreateView):
    model = Patient
    fields = ['first_name', 'last_name', 'cpf', 'birth_date', 'phone', 'email']
    template_name = 'clinic/generic_form.html'
    success_url = reverse_lazy('patient-list')

@group_required('Administradores','Profissionais','Financeiro')
class PatientUpdateView(LoginRequiredMixin, CrudMixin, UpdateView):
    model = Patient
    fields = ['first_name', 'last_name', 'cpf', 'birth_date', 'phone', 'email']
    template_name = 'clinic/generic_form.html'
    success_url = reverse_lazy('patient-list')

@group_required('Administradores','Profissionais','Financeiro')
class PatientDeleteView(LoginRequiredMixin, CrudMixin, DeleteView):
    model = Patient
    template_name = 'clinic/generic_confirm_delete.html'
    success_url = reverse_lazy('patient-list')

@group_required('Administradores','Profissionais')
class PatientHistoryView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'clinic/patient_history.html'
    context_object_name = 'appointments'

    def get_queryset(self):
        return Appointment.objects.filter(patient_id=self.kwargs['pk']).order_by('-date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient = Patient.objects.get(pk=self.kwargs['pk'])
        context['patient'] = patient
        
        # Data for Weight Chart
        weight_data = Appointment.objects.filter(
            patient=patient, 
            weight__isnull=False
        ).order_by('date')
        
        context['weight_labels'] = [a.date.strftime("%d/%m/%Y") for a in weight_data]
        context['weight_values'] = [float(a.weight) for a in weight_data]

        # Data for Body Fat Percentage Chart
        body_fat_data = Appointment.objects.filter(
            patient=patient,
            body_fat_percentage__isnull=False
        ).order_by('date')
        
        context['body_fat_labels'] = [a.date.strftime("%d/%m/%Y") for a in body_fat_data]
        context['body_fat_values'] = [float(a.body_fat_percentage) for a in body_fat_data]  
        
        # Patient Payments
        context['payments'] = Payment.objects.filter(patient=patient).order_by('-payment_date')
        
        return context
