from django.db import models

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
