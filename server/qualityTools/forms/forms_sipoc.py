from django import forms
from qualityTools.models.models_sipoc import MapeamentoSIPOC, FerramentaSIPOC

class MapeamentoSIPOCForm(forms.ModelForm):
    class Meta:
        model = MapeamentoSIPOC
        fields = ['macroprocesso', 'versao', 'vigencia', 'gestor']

class FerramentaSIPOCForm(forms.ModelForm):
    class Meta:
        model = FerramentaSIPOC
        fields = [
            'mapeamento',
            'missao',
            'sistema',
            'equipe',
            'equipamentos',
            'produto',
            'resultado',
            'fornecedor',
            'entrada',
            'processo',
            'saida',
            'cliente'
        ]
