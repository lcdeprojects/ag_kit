from django.db import models
from django.contrib.auth.models import User
from .patient import Patient

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Paciente")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Responsável")
    date = models.DateTimeField(verbose_name="Data e Hora")
    body_fat_percentage = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Gordura Corporal (%)")
    # Clinical Records
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True, verbose_name="Peso (kg)")
    clinical_notes = models.TextField(blank=True, verbose_name="Notas Clínicas")
    prescription = models.TextField(blank=True, verbose_name="Prescrição")

    def __str__(self):
        return f"Consulta: {self.patient.name}"

    class Meta:
        verbose_name = "Consulta"
        verbose_name_plural = "Consultas"
