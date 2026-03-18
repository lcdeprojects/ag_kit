import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aliada_root.settings')
django.setup()

from clinic.models import Patient, Payment

def check_payments():
    patients = Patient.objects.all()
    print(f"Total de pacientes: {patients.count()}")
    for p in patients:
        payments = Payment.objects.filter(patient=p)
        print(f"Paciente: {p.name} (ID: {p.id}) - Pagamentos: {payments.count()}")
        for pay in payments:
            print(f"  - Valor: {pay.amount}, Data: {pay.payment_date}")

if __name__ == "__main__":
    check_payments()
