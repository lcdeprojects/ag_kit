from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    # name column was replaced; property kept for template compatibility
    first_name = models.CharField(max_length=100, verbose_name="Nome", default="")
    last_name = models.CharField(max_length=100, verbose_name="Sobrenome", default="")
    cpf = models.CharField(max_length=14, unique=True, verbose_name="CPF")
    birth_date = models.DateField(verbose_name="Data de Nascimento")
    phone = models.CharField(max_length=20, verbose_name="Telefone")
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}".strip()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"

class Professional(models.Model):
    TYPES = (
        ('doctor', 'Médico'),
        ('nutritionist', 'Nutricionista'),
    )
    name = models.CharField(max_length=200, verbose_name="Nome")
    registration_number = models.CharField(max_length=50, unique=True, verbose_name="CRM/Registro")
    specialty = models.CharField(max_length=100, verbose_name="Especialidade")
    professional_type = models.CharField(max_length=20, choices=TYPES, verbose_name="Tipo")

    def __str__(self):
        return f"{self.get_professional_type_display()}: {self.name}"

    class Meta:
        verbose_name = "Profissional"
        verbose_name_plural = "Profissionais"

from django.utils import timezone
from datetime import timedelta

class HealthPlan(models.Model):
    title = models.CharField(max_length=100, verbose_name="Título do Plano")
    description = models.TextField(blank=True, verbose_name="Descrição")
    validity_days = models.IntegerField(default=30, verbose_name="Dias de Validade")
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Valor")
    percentage_medical_plan = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Percentual Médico")
    percentage_nutrition_plan = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Percentual Nutricionista")
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Plano de Saúde"
        verbose_name_plural = "Planos de Saúde"

class Payment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, verbose_name="Paciente")
    plan = models.ForeignKey(HealthPlan, on_delete=models.SET_NULL, null=True, verbose_name="Plano")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Valor")
    payment_date = models.DateField(verbose_name="Data do Pagamento")
    notes = models.TextField(blank=True, verbose_name="Observações")

    @property
    def amount_medical_plan(self):
        if self.plan:
            return (self.amount * self.plan.percentage_medical_plan) / 100
        return 0

    @property
    def amount_nutrition_plan(self):
        if self.plan:
            return (self.amount * self.plan.percentage_nutrition_plan) / 100
        return 0
    
    
    @property
    def expiration_date(self):
        if self.plan and self.payment_date:
            return self.payment_date + timedelta(days=self.plan.validity_days)
        return None

    @property
    def days_remaining(self):
        exp = self.expiration_date
        if exp:
            delta = exp - timezone.now().date()
            return delta.days
        return -999

    @property
    def status(self):
        remaining = self.days_remaining
        if remaining < 0:
            return 'expired'
        elif remaining <= 20:
            return 'warning'
        return 'active'

    def __str__(self):
        return f"Pagamento {self.patient.name} - {self.payment_date}"

    class Meta:
        verbose_name = "Pagamento"
        verbose_name_plural = "Pagamentos"

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
