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

        def __init__(self, *args, **kwargs):
            super(FerramentaSWOT, self).__init__(*args, **kwargs)
            if self.instance and self.instance.pk:
                # Verifique se a instância contém valores e se os campos estão corretamente populados
                self.fields['oportunidade_melhoria'].initial = self.instance.oportunidade_melhoria
                self.fields['notificacao_evento_adverso'].initial = self.instance.notificacao_evento_adverso