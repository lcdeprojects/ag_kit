from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from .base import CrudMixin
from ..decorator import group_required
from ..models import Patient, Anamnese

@group_required('Administradores','Profissionais')
class AnamneseDetailView(LoginRequiredMixin, DetailView):
    model = Anamnese
    template_name = 'clinic/anamnese_detail.html'
    context_object_name = 'anamnese'

    def get_object(self, queryset=None):
        patient_pk = self.kwargs.get('pk')
        try:
            return Anamnese.objects.get(patient_id=patient_pk)
        except Anamnese.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        if self.object is None:
            return redirect('anamnese-create', pk=self.kwargs.get('pk'))
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(pk=self.kwargs.get('pk'))
        return context

@group_required('Administradores','Profissionais')
class AnamneseCreateView(LoginRequiredMixin, CrudMixin, CreateView):
    model = Anamnese
    fields = [
        'altura', 'peso', 'mora_com_quem', 'tem_dia_lista_compras', 
        'como_e_lista_compras', 'fenotipo', 'o_que_incomoda', 
        'imc_avaliacao', 'circunferencia_abdominal', 'objetivo', 
        'treino', 'intestino', 'aversao', 'organizacao', 'historico_peso',
        'cidade', 'estado', 'profissao', 'idade',
        'toma_agua', 'medicamentos', 'sono', 'doenca_intolerancia'
    ]
    template_name = 'clinic/anamnese_form.html'
    
    def form_valid(self, form):
        form.instance.patient_id = self.kwargs.get('pk')
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('anamnese-detail', kwargs={'pk': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(pk=self.kwargs.get('pk'))
        context['verbose_name'] = 'Anamnese'
        return context

@group_required('Administradores','Profissionais')
class AnamneseUpdateView(LoginRequiredMixin, CrudMixin, UpdateView):
    model = Anamnese
    fields = [
        'altura', 'peso', 'mora_com_quem', 'tem_dia_lista_compras', 
        'como_e_lista_compras', 'fenotipo', 'o_que_incomoda', 
        'imc_avaliacao', 'circunferencia_abdominal', 'objetivo', 
        'treino', 'intestino', 'aversao', 'organizacao', 'historico_peso',
        'cidade', 'estado', 'profissao', 'idade',
        'toma_agua', 'medicamentos', 'sono', 'doenca_intolerancia'
    ]
    template_name = 'clinic/anamnese_form.html'

    def get_object(self, queryset=None):
        return Anamnese.objects.get(patient_id=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse_lazy('anamnese-detail', kwargs={'pk': self.kwargs.get('pk')})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['patient'] = Patient.objects.get(pk=self.kwargs.get('pk'))
        context['verbose_name'] = 'Anamnese'
        return context

@group_required('Administradores','Profissionais')
class AnamneseDeleteView(LoginRequiredMixin, CrudMixin, DeleteView):
    model = Anamnese
    template_name = 'clinic/generic_confirm_delete.html'
    
    def get_object(self, queryset=None):
        return Anamnese.objects.get(patient_id=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse_lazy('patient-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['verbose_name'] = 'Anamnese'
        return context
