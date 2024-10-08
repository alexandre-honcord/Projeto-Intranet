from django import forms
from qualityTools.models.models_swot import FerramentaSWOT


class FerramentaSWOTForm(forms.ModelForm):
    class Meta:
        model = FerramentaSWOT
        fields = ['oportunidade_melhoria', 'notificacao_evento_adverso', 'forcas', 'fraquezas', 'oportunidades', 'ameacas']
        widgets = {
            'oportunidade_melhoria': forms.Select(attrs={'class': 'form-control'}),
            'notificacao_evento_adverso': forms.Select(attrs={'class': 'form-control'}),
            'forcas': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'fraquezas': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'oportunidades': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
            'ameacas': forms.Textarea(attrs={'class': 'form-control', 'rows': 2}),
        }