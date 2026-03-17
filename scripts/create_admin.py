import os
import django

# Configura o ambiente Django ANTES de importar qualquer model
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'aliada_root.settings')
django.setup()

# Agora podemos importar os models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

def create_admin():
    User = get_user_model()
    username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'admin')
    email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'lcdeksb@gmail.com')
    password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'Aliada@admin26')

    # Garantir que o grupo Administradores existe
    admin_group, _ = Group.objects.get_or_create(name='Administradores')
    Group.objects.get_or_create(name='Profissionais')

    # Cria ou atualiza o superusuário
    user, created = User.objects.get_or_create(username=username, defaults={'email': email})
    
    if created or not user.is_superuser:
        user.is_superuser = True
        user.is_staff = True
        user.set_password(password)
        user.save()
        print(f"✅ Superusuário '{username}' criado/atualizado com sucesso!")
    
    # Garantir que o admin está no grupo
    user.groups.add(admin_group)
    print(f"✅ Usuário '{username}' adicionado ao grupo 'Administradores'.")

if __name__ == "__main__":
    create_admin()
