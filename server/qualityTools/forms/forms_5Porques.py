from django import forms
from qualityTools.models.models_5Porques import Ferramenta5Porques

class Ferramenta5PorquesForm(forms.ModelForm):
    class Meta:
        model = Ferramenta5Porques
        fields = ['oportunidade_melhoria', 'notificacao_evento_adverso', 'porque1', 'porque2', 'porque3', 'porque4', 'porque5']
        widgets = {
            'oportunidade_melhoria': forms.Select(attrs={'class': 'form-control'}),
            'notificacao_evento_adverso': forms.Select(attrs={'class': 'form-control'}),
            'porque1': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'porque2': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'porque3': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'porque4': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'porque5': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }

    def __init__(self, *args, **kwargs):
        super(Ferramenta5PorquesForm, self).__init__(*args, **kwargs)
        if self.instance and self.instance.pk:
            # Verifique se a instância contém valores e se os campos estão corretamente populados
            self.fields['oportunidade_melhoria'].initial = self.instance.oportunidade_melhoria
            self.fields['notificacao_evento_adverso'].initial = self.instance.notificacao_evento_adverso

