from django.db import models
from quality.models import Opportunity, Notification

class Ferramenta5Porques(models.Model):
    oportunidade_melhoria = models.ForeignKey(Opportunity, on_delete=models.CASCADE, related_name='ferramentas_5porques', null=True, blank=True)
    notificacao_evento_adverso = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name='ferramentas_5porques', null=True, blank=True)
    porque1 = models.TextField(blank=True, null=True)
    porque2 = models.TextField(blank=True, null=True)
    porque3 = models.TextField(blank=True, null=True)
    porque4 = models.TextField(blank=True, null=True)
    porque5 = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.notificacao_evento_adverso:
            return f"{self.notificacao_evento_adverso} - 5 Porquês"
        return f"{self.oportunidade_melhoria} - 5 Porquês"
