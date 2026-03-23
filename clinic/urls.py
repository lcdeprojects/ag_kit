from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('export-payment-report/', views.export_payment_report, name='payment_report'),
    
    # Patient URLs
    path('pacientes/', views.PatientListView.as_view(), name='patient-list'),
    path('pacientes/novo/', views.PatientCreateView.as_view(), name='patient-create'),
    path('pacientes/<int:pk>/editar/', views.PatientUpdateView.as_view(), name='patient-update'),
    path('pacientes/<int:pk>/excluir/', views.PatientDeleteView.as_view(), name='patient-delete'),
    path('pacientes/<int:pk>/historico/', views.PatientHistoryView.as_view(), name='patient-history'),
    
    # Professional URLs
    path('profissionais/', views.ProfessionalListView.as_view(), name='professional-list'),
    path('profissionais/novo/', views.ProfessionalCreateView.as_view(), name='professional-create'),
    path('profissionais/<int:pk>/editar/', views.ProfessionalUpdateView.as_view(), name='professional-update'),
    path('profissionais/<int:pk>/excluir/', views.ProfessionalDeleteView.as_view(), name='professional-delete'),
    
    # HealthPlan URLs
    path('planos/', views.HealthPlanListView.as_view(), name='healthplan-list'),
    path('planos/novo/', views.HealthPlanCreateView.as_view(), name='healthplan-create'),
    path('planos/<int:pk>/editar/', views.HealthPlanUpdateView.as_view(), name='healthplan-update'),
    path('planos/<int:pk>/excluir/', views.HealthPlanDeleteView.as_view(), name='healthplan-delete'),
    
    # Payment URLs
    path('pagamentos/', views.PaymentListView.as_view(), name='payment-list'),
    path('pagamentos/novo/', views.PaymentCreateView.as_view(), name='payment-create'),
    path('pagamentos/<int:pk>/editar/', views.PaymentUpdateView.as_view(), name='payment-update'),
    path('pagamentos/<int:pk>/excluir/', views.PaymentDeleteView.as_view(), name='payment-delete'),
    
    # Appointment URLs
    path('consultas/', views.AppointmentListView.as_view(), name='appointment-list'),
    path('consultas/novo/', views.AppointmentCreateView.as_view(), name='appointment-create'),
    path('consultas/<int:pk>/', views.AppointmentDetailView.as_view(), name='appointment-detail'),
    path('consultas/<int:pk>/editar/', views.AppointmentUpdateView.as_view(), name='appointment-update'),
    path('consultas/<int:pk>/excluir/', views.AppointmentDeleteView.as_view(), name='appointment-delete'),
    path('anexos/<int:pk>/excluir/', views.AttachmentDeleteView.as_view(), name='attachment-delete'),
    path('today/', views.today, name='today'),
    
    # Agenda URL
    path('agenda/', views.AgendaView.as_view(), name='agenda'),

    #Acessos
    path('denied/', views.denied, name='denied'),
    path('settings/', views.settings, name='settings'),
    path('user/create/', views.UserCreateView.as_view(), name='user-create'),
    path('user/', views.UserListView.as_view(), name='user-list'),
    path('user/<int:pk>/editar/', views.UserUpdateView.as_view(), name='user-update'),
    path('user/<int:pk>/reset-password/', views.user_password_reset, name='user-password-reset'),]
