from django import forms
from qualityTools.models.models_sipoc import MapeamentoSIPOC, FerramentaSIPOC

class MapeamentoSIPOCForm(forms.ModelForm):
    class Meta:
        model = MapeamentoSIPOC
        fields = ['macroprocesso', 'versao', 'vigencia', 'gestor']
        widgets = {
            'macroprocesso': forms.Textarea(attrs={'class': 'form-control'}),
            'versao': forms.TextInput(attrs={'class': 'form-control'}),
            'vigencia': forms.TextInput(attrs={'class': 'form-control'}),
            'gestor': forms.TextInput(attrs={'class': 'form-control'}),
        }

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
