from django.db import models
from .appointment import Appointment

class AppointmentAttachment(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE, related_name='attachments', verbose_name="Consulta")
    file = models.FileField(upload_to='appointments/attachments/', verbose_name="Arquivo")
    description = models.CharField(max_length=255, blank=True, verbose_name="Descrição")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Anexo de {self.appointment.patient.name} - {self.file.name}"

    class Meta:
        verbose_name = "Anexo de Consulta"
        verbose_name_plural = "Anexos de Consulta"
