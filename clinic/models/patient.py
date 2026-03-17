from django.db import models

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
