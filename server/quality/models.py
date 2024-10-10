# quality/models.py

from django.db import models
from django.contrib.auth.models import User

class Grupos(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gestor = models.BooleanField(default=False)
    qualidade = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Grupo"  # Nome singular
        verbose_name_plural = "Grupos"  # Nome plural

    def __str__(self):
        return self.user.username

class Client(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
TIPO_CHOICES = [
    ('sugestao', 'Sugestão'),
    ('problema', 'Problema Identificado'),
    ('inovacao', 'Oportunidade de Inovação'),
    ('eficiencia', 'Melhoria de Eficiência'),
    ('custos', 'Redução de Custos'),
    ('qualidade', 'Aumento de Qualidade'),
    ('experiencia', 'Aprimoramento de Experiência do Cliente'),
    ('tecnologia', 'Implementação de Tecnologia'),
    ('treinamento', 'Capacitação ou Treinamento'),
    ('sustentabilidade', 'Sustentabilidade'),

    ]

PRIORIDADE_CHOICES = [
        ('Baixa', 'Baixa'),
        ('Média', 'Média'),
        ('Alta', 'Alta'),
    ]

class Opportunity(models.Model):
    
    title = models.CharField(max_length=100, verbose_name='Titulo')
    description = models.TextField( verbose_name='Descrição')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Criado por:')
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True, verbose_name='Data de Finalização')
    tipo = models.CharField(max_length=50,null=False, blank=False, choices=TIPO_CHOICES, default='Melhoria')
    prioridade = models.CharField(max_length=50, choices=PRIORIDADE_CHOICES, default='Média')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Setor')
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Status')

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.status_id:
            pendente_status = Status.objects.get(name='Pendente')  # Busca o status 'Pendente'
            self.status = pendente_status
        super().save(*args, **kwargs)
    
class Notification(models.Model):

    title = models.CharField(max_length=100, verbose_name='Titulo')
    content = models.TextField(verbose_name='Descrição')
    created_at = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True, verbose_name='Data de Finalização')
    identified_by = models.CharField(max_length=100, blank=True, null=True, verbose_name='Caso queira se identificar')
    priority = models.CharField(max_length=50, choices=PRIORIDADE_CHOICES, default='Média', verbose_name='Prioridade')
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Cliente')
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Setor')
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Status')

    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.status_id:
            pendente_status = Status.objects.get(name='Pendente')  # Busca o status 'Pendente'
            self.status = pendente_status
        super().save(*args, **kwargs)
