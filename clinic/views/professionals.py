from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .base import CrudMixin
from ..decorator import group_required
from ..models import Professional

@group_required('Administradores')
class ProfessionalListView(LoginRequiredMixin, ListView):
    model = Professional
    template_name = 'clinic/professional_list.html'
    context_object_name = 'professionals'

@group_required('Administradores')
class ProfessionalCreateView(LoginRequiredMixin, CrudMixin, CreateView):
    model = Professional
    fields = ['name', 'registration_number', 'specialty', 'professional_type']
    template_name = 'clinic/generic_form.html'
    success_url = reverse_lazy('professional-list')

@group_required('Administradores')
class ProfessionalUpdateView(LoginRequiredMixin, CrudMixin, UpdateView):
    model = Professional
    fields = ['name', 'registration_number', 'specialty', 'professional_type']
    template_name = 'clinic/generic_form.html'
    success_url = reverse_lazy('professional-list')

@group_required('Administradores')
class ProfessionalDeleteView(LoginRequiredMixin, CrudMixin, DeleteView):
    model = Professional
    template_name = 'clinic/generic_confirm_delete.html'
    success_url = reverse_lazy('professional-list')
