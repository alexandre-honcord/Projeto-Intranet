from django.db import models

class MapeamentoSIPOC(models.Model):
    macroprocesso = models.CharField(max_length=255)
    versao = models.CharField(max_length=255)
    vigenca = models.CharField(max_length=255)
    gestor = models.CharField(max_length=255)

    def __str__(self):
        return self.macroprocesso
    
class FerramentaSIPOC(models.Model):
    mapeamento = models.ForeignKey(MapeamentoSIPOC, on_delete=models.CASCADE, related_name='ferramentas_sipoc', null=True, blank=True)
    missao = models.TextField()
    sistema = models.TextField()
    equipe = models.TextField()
    equipamentos = models.TextField()

    produto = models.TextField()
    resultado = models.TextField()

    fornecedor = models.TextField()
    entrada = models.TextField()
    processo = models.ImageField(upload_to='qualityTools/processosSIPOC/photos/')
    saida = models.TextField()
    cliente = models.TextField()

    def __str__(self):
        return f"{self.mapeamento} - SIPOC"