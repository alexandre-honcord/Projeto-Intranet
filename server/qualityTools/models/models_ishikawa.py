from django.db import models
from quality.models import Opportunity, Notification


class FerramentaIshikawa(models.Model):
    oportunidade_melhoria = models.ForeignKey(Opportunity, on_delete=models.CASCADE, related_name='ferramentas_ishikawa', null=True, blank=True)
    notificacao_evento_adverso = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name='ferramentas_ishikawa', null=True, blank=True)
    problema = models.TextField()
    causas = models.TextField()
    metodo = models.TextField(blank=True, null=True)
    mao_de_obra = models.TextField(blank=True, null=True)
    maquina = models.TextField(blank=True, null=True)
    material = models.TextField(blank=True, null=True)
    medicao = models.TextField(blank=True, null=True)
    meio_ambiente = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.notificacao_evento_adverso:
            return f"{self.notificacao_evento_adverso} - {self.problema}"
        return f"{self.oportunidade_melhoria} - {self.problema}"