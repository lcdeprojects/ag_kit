from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db import models
from .base import CrudMixin
from ..decorator import group_required
from ..models import Appointment, AppointmentAttachment

@group_required('Administradores','Profissionais')
class AppointmentListView(LoginRequiredMixin, ListView):
    model = Appointment
    template_name = 'clinic/appointment_list.html'
    context_object_name = 'appointments'
    paginate_by = 6

    def get_queryset(self):
        qs = Appointment.objects.all().order_by('-date')
        
        # Pesquisa por nome do paciente
        q = self.request.GET.get('q')
        if q:
            qs = qs.filter(models.Q(patient__first_name__icontains=q) | models.Q(last_name__icontains=q))
            
        # Filtro por data
        date_filter = self.request.GET.get('date')
        if date_filter:
            qs = qs.filter(date__date=date_filter)
            
        # Filtro por responsável
        user_filter = self.request.GET.get('user')
        if user_filter:
            qs = qs.filter(user_id=user_filter)
            
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['users'] = User.objects.all().order_by('first_name', 'username')
        context['current_q'] = self.request.GET.get('q', '')
        context['current_date'] = self.request.GET.get('date', '')
        context['current_user'] = self.request.GET.get('user', '')
        return context

@group_required('Administradores','Profissionais')
class AppointmentCreateView(LoginRequiredMixin, CrudMixin, CreateView):
    model = Appointment
    fields = ['patient', 'date', 'weight', 'body_fat_percentage', 'clinical_notes', 'prescription']
    template_name = 'clinic/generic_form.html'
    
    def get_success_url(self):
        return reverse_lazy('patient-history', kwargs={'pk': self.object.patient.pk})

    def get_initial(self):
        initial = super().get_initial()
        patient_id = self.request.GET.get('patient')
        if patient_id:
            initial['patient'] = patient_id
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        
        # Handle attachments
        files = self.request.FILES.getlist('attachments')
        for f in files:
            AppointmentAttachment.objects.create(appointment=self.object, file=f)
            
        return response

@group_required('Administradores','Profissionais')
class AppointmentUpdateView(LoginRequiredMixin, CrudMixin, UpdateView):
    model = Appointment
    fields = ['patient', 'date', 'weight', 'body_fat_percentage', 'clinical_notes', 'prescription']
    template_name = 'clinic/generic_form.html'

    def get_success_url(self):
        return reverse_lazy('patient-history', kwargs={'pk': self.object.patient.pk})

    def form_valid(self, form):
        response = super().form_valid(form)
        
        # Handle attachments
        files = self.request.FILES.getlist('attachments')
        for f in files:
            AppointmentAttachment.objects.create(appointment=self.object, file=f)
            
        return response

@group_required('Administradores','Profissionais')
class AttachmentDeleteView(LoginRequiredMixin, DeleteView):
    model = AppointmentAttachment
    template_name = 'clinic/generic_confirm_delete.html'
    
    def get_success_url(self):
        return reverse_lazy('patient-history', kwargs={'pk': self.object.appointment.patient.pk})

@group_required('Administradores','Profissionais')
class AppointmentDetailView(LoginRequiredMixin, CrudMixin, DeleteView): # Inheriting from DeleteView just for CrudMixin context, better use DetailView
    model = Appointment
    template_name = 'clinic/appointment_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = 'Detalhes da Consulta'
        return context

@group_required('Administradores','Profissionais')
class AppointmentDeleteView(LoginRequiredMixin, CrudMixin, DeleteView):
    model = Appointment
    template_name = 'clinic/generic_confirm_delete.html'
    success_url = reverse_lazy('appointment-list')

class AgendaView(LoginRequiredMixin, CrudMixin, ListView):
    # Using ListView to inherit CrudMixin context, even though we won't list a specific model here
    # We'll override the model name in the template
    model = Appointment 
    template_name = 'clinic/agenda.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = 'Agenda'
        return context
