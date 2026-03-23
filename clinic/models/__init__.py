from .patient import Patient
from .professional import Professional
from .healthplan import HealthPlan
from .payment import Payment
from .appointment import Appointment
from .attachment import AppointmentAttachment
from auditlog.registry import auditlog

auditlog.register(Patient)
auditlog.register(Professional)
auditlog.register(HealthPlan)
auditlog.register(Payment)
auditlog.register(Appointment)
auditlog.register(AppointmentAttachment)

__all__ = ['Patient', 'Professional', 'HealthPlan', 'Payment', 'Appointment', 'AppointmentAttachment']
