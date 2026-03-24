import sys
import os
sys.path.append(os.getcwd())
import django
from django.utils import timezone
from datetime import timedelta

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aliada_root.settings')
django.setup()

from clinic.models import Payment, HealthPlan, Patient
from django.db.models import F, ExpressionWrapper, DateField, DurationField
from django.db.models.functions import Cast

def verify_queryset():
    print("Testing QuerySet annotation logic...")
    today = timezone.now().date()
    
    # We don't necessarily need to create objects if we just want to verify the query construction
    # But let's try a simple test if DB is accessible
    try:
        qs = Payment.objects.annotate(
            annotated_expiration=ExpressionWrapper(
                F('payment_date') + Cast(F('plan__validity_days') * 86400000000, DurationField()),
                output_field=DateField()
            )
        )
        # Check if we can filter by it
        count = qs.filter(annotated_expiration__lt=today).count()
        print(f"Query executed successfully. Found {count} expired payments.")
    except Exception as e:
        print(f"Error executing query: {e}")

if __name__ == "__main__":
    verify_queryset()
