from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .base import CrudMixin
from ..decorator import group_required
from ..models import HealthPlan

@group_required('Administradores')
class HealthPlanListView(LoginRequiredMixin, ListView):
    model = HealthPlan
    template_name = 'clinic/healthplan_list.html'
    context_object_name = 'plans'

@group_required('Administradores')
class HealthPlanCreateView(LoginRequiredMixin, CrudMixin, CreateView):
    model = HealthPlan
    fields = ['title', 'description', 'validity_days', 'amount', 'percentage_medical_plan', 'percentage_nutrition_plan']
    template_name = 'clinic/generic_form.html'
    success_url = reverse_lazy('healthplan-list')

@group_required('Administradores')
class HealthPlanUpdateView(LoginRequiredMixin, CrudMixin, UpdateView):
    model = HealthPlan
    fields = ['title', 'description', 'validity_days', 'amount', 'percentage_medical_plan', 'percentage_nutrition_plan']
    template_name = 'clinic/generic_form.html'
    success_url = reverse_lazy('healthplan-list')

@group_required('Administradores')
class HealthPlanDeleteView(LoginRequiredMixin, CrudMixin, DeleteView):
    model = HealthPlan
    template_name = 'clinic/generic_confirm_delete.html'
    success_url = reverse_lazy('healthplan-list')
