from django.db import models
from .patient import Patient

class Anamnese(models.Model):
    CHOICES_SIM_NAO = [
        ('Sim', 'Sim'),
        ('Não', 'Não'),
    ]

    CHOICES_IMC = [
        ('Abaixo do peso', 'Abaixo do peso'),
        ('Peso normal', 'Peso normal'),
        ('Sobrepeso', 'Sobrepeso'),
        ('Obesidade Grau I', 'Obesidade Grau I'),
        ('Obesidade Grau II', 'Obesidade Grau II'),
        ('Obesidade Grau III', 'Obesidade Grau III'),
    ]

    CHOICES_INTESTINO = [
        ('Funciona bem', 'Funciona bem'),
        ('Não funciona bem', 'Não funciona bem'),
    ]

    patient = models.OneToOneField(Patient, on_delete=models.CASCADE, related_name='anamnese', verbose_name="Paciente")
    
    # Questionnaire Fields
    altura = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Altura (m)")
    peso = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Peso (kg)")
    mora_com_quem = models.CharField(max_length=100, blank=True, null=True, verbose_name="Mora com quem?")
    tem_dia_lista_compras = models.CharField(max_length=3, choices=CHOICES_SIM_NAO, verbose_name="Tem dia para fazer lista de compras?")
    como_e_lista_compras = models.TextField(verbose_name="Como é sua lista de compras?")
    fenotipo = models.TextField(verbose_name="Fenótipo?")
    o_que_incomoda = models.TextField(verbose_name="O que incomoda você hoje?")
    imc_avaliacao = models.CharField(max_length=20, choices=CHOICES_IMC, verbose_name="IMC/Avaliação")
    circunferencia_abdominal = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Circunferência Abdominal (cm)")
    objetivo = models.TextField(verbose_name="Qual seu objetivo hoje?")
    treino = models.TextField(blank=False, null=True, verbose_name="Treino?")
    intestino = models.CharField(max_length=100, blank=False, null=True, verbose_name="Intestino?")
    aversao = models.CharField(max_length=100, blank=False, null=True, verbose_name="Aversão?")
    organizacao = models.TextField(blank=False, null=True, verbose_name="Como pretende se organizar?")
    historico_peso = models.TextField(blank=False, null=True, verbose_name="Histórico de Evolução de Peso")
    cidade = models.CharField(max_length=100, blank=False, null=True, verbose_name="Cidade")
    estado = models.CharField(max_length=2, blank=False, null=True, verbose_name="Estado")
    profissao = models.CharField(max_length=100, blank=False, null=True, verbose_name="Profissão")
    idade = models.IntegerField(blank=False, null=True, verbose_name="Idade")
    toma_agua = models.CharField(max_length=100, blank=False, null=True, verbose_name="Toma água?")
    medicamentos = models.CharField(max_length=100, blank=False, null=True, verbose_name="Medicamentos?")
    sono = models.CharField(max_length=100, blank=False, null=True, verbose_name="Sono?")
    doenca_intolerancia = models.CharField(max_length=100, blank=False, null=True, verbose_name="Doença/Intolerância?")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Anamnese: {self.patient.name}"

    class Meta:
        verbose_name = "Anamnese"
        verbose_name_plural = "Anamneses"
