from django.db import models

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
