from django.db import models
from quality.models import Opportunity, Notification


class Ferramenta5W2H(models.Model):
    oportunidade_melhoria = models.ForeignKey(Opportunity, on_delete=models.CASCADE, related_name='ferramentas_5w2h', null=True, blank=True)
    notificacao_evento_adverso = models.ForeignKey(Notification, on_delete=models.CASCADE, related_name='ferramentas_5w2h', null=True, blank=True)
    what = models.TextField()
    why = models.TextField()
    where = models.TextField()
    when = models.DateTimeField()
    who = models.TextField()
    how = models.TextField()
    how_much = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        if self.notificacao_evento_adverso:
            return f"{self.notificacao_evento_adverso} - {self.what}"
        return f"{self.oportunidade_melhoria} - {self.what}"