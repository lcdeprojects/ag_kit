from django.db import models
from django.utils import timezone
from datetime import timedelta
from .patient import Patient
from .healthplan import HealthPlan

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
