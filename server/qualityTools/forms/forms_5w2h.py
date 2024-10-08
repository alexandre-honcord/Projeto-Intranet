from django import forms
from qualityTools.models.models_5w2h import Ferramenta5W2H

class Ferramenta5W2HForm(forms.ModelForm):
    
    class Meta:
        model = Ferramenta5W2H
        fields = '__all__'
        widgets = {
            'oportunidade_melhoria': forms.Select(attrs={'class': 'form-control'}),
            'notificacao_evento_adverso': forms.Select(attrs={'class': 'form-control'}),
            'what': forms.TextInput(attrs={'class': 'form-control'}),
            'why': forms.TextInput(attrs={'class': 'form-control'}),
            'where': forms.TextInput(attrs={'class': 'form-control'}),
            'when': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'who': forms.TextInput(attrs={'class': 'form-control'}),
            'how': forms.TextInput(attrs={'class': 'form-control'}),
            'how_much': forms.TextInput(attrs={'class': 'form-control', 'type': 'number', 'step': '0.01'}),
        }