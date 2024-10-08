from django import forms
from qualityTools.models.models_ishikawa import  FerramentaIshikawa

class FerramentaIshikawaForm(forms.ModelForm):
    class Meta:
        model = FerramentaIshikawa
        fields = ['oportunidade_melhoria', 'notificacao_evento_adverso', 'problema', 'causas', 'metodo', 'mao_de_obra', 'maquina', 'material', 'medicao', 'meio_ambiente']
        widgets = {
            'oportunidade_melhoria': forms.Select(attrs={'class': 'form-control'}),
            'notificacao_evento_adverso': forms.Select(attrs={'class': 'form-control'}),
            'problema': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'causas': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'metodo': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'mao_de_obra': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'maquina': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'material': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'medicao': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'meio_ambiente': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
        
        def __init__(self, *args, **kwargs):
            super(FerramentaIshikawa, self).__init__(*args, **kwargs)
            if self.instance and self.instance.pk:
                # Verifique se a instância contém valores e se os campos estão corretamente populados
                self.fields['oportunidade_melhoria'].initial = self.instance.oportunidade_melhoria
                self.fields['notificacao_evento_adverso'].initial = self.instance.notificacao_evento_adverso