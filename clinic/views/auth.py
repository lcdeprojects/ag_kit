from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
import secrets
import string
from .base import CrudMixin
from ..decorator import group_required

@group_required('Administradores')
class UserCreateView(LoginRequiredMixin, CrudMixin, CreateView):
    model = User
    fields = ['username', 'email', 'password',  'first_name', 'last_name', 'groups']
    template_name = 'clinic/generic_form.html'
    success_url = reverse_lazy('user-list')

    def form_valid(self, form):
        # Hash the password before saving
        user = form.save(commit=False)
        user.set_password(form.cleaned_data['password'])
        user.save()
        # Save M2M fields (groups)
        form.save_m2m()
        return redirect(self.success_url)

@group_required('Administradores')
class UserListView(LoginRequiredMixin, CrudMixin, ListView):
    model = User
    template_name = 'clinic/user_list.html'
    context_object_name = 'users'

    def get_queryset(self):
        return User.objects.all().order_by('first_name', 'username')

@group_required('Administradores')
class UserUpdateView(LoginRequiredMixin, CrudMixin, UpdateView):
    model = User
    fields = ['username', 'email', 'first_name', 'last_name', 'groups']
    template_name = 'clinic/generic_form.html'
    success_url = reverse_lazy('user-list')

    def form_valid(self, form):
        return super().form_valid(form)

@login_required
@group_required('Administradores')
def user_password_reset(request, pk):
    user = User.objects.get(pk=pk)
    # Generate random password
    alphabet = string.ascii_letters + string.digits
    temp_password = ''.join(secrets.choice(alphabet) for i in range(8))
    
    user.set_password(temp_password)
    user.save()
    
    messages.success(request, f'Senha do usuário {user.username} resetada com sucesso para: {temp_password}')
    return redirect('user-list')
