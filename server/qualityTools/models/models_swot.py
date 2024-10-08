from django.db import models
from quality.models import Opportunity, Notification


class FerramentaSWOT(models.Model):
    oportunidade_melhoria = models.ForeignKey(Opportunity, on_delete=models.CASCADE, related_name='ferramentas_swot', null=True, blank=True)
    notificacao_evento_adverso = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name='ferramentas_swot', null=True, blank=True)
    forcas = models.TextField(blank=True, null=True)
    fraquezas = models.TextField(blank=True, null=True)
    oportunidades = models.TextField(blank=True, null=True)
    ameacas = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.notificacao_evento_adverso:
            return f"{self.notificacao_evento_adverso} - SWOT"
        return f"{self.oportunidade_melhoria} - SWOT"