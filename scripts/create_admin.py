import os
import django
from django.contrib.auth import get_user_model

# Configura o ambiente Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aliada_root.settings')
django.setup()

def create_admin():
    User = get_user_model()
    username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'lcdeksb@gmail.com')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'Aliada@admin26')

    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username, email, password)
        print(f"✅ Superusuário '{username}' criado com sucesso!")
    else:
        print(f"ℹ️ Superusuário '{username}' já existe. Pulando criação.")

if __name__ == "__main__":
    create_admin()
