# core/forms.py
from django import forms
from .models import Opportunity, Notification
from django.contrib.auth.models import User

class OpportunityForm(forms.ModelForm):
    class Meta:
        model = Opportunity
        fields = ['title', 'description', 'tipo', 'prioridade', 'location']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'tipo': forms.Select(attrs={'class': 'form-control'}),
            'prioridade': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Remove o usuário dos kwargs
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user and self.user.is_authenticated:
            instance.created_by = self.user  # Atribui o usuário autenticado
        else:
            instance.created_by = None  # Armazena como anônimo se o usuário não estiver logado
        if commit:
            instance.save()
        return instance

class NotificationForm(forms.ModelForm):
    anonymous = forms.BooleanField(required=False, label="Marque para permanecer anônimo.")  # Novo campo para permitir anonimato

    class Meta:
        model = Notification
        fields = ['title', 'content', 'priority', 'client', 'location']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'priority': forms.Select(attrs={'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)  # Captura o usuário autenticado
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.cleaned_data.get('anonymous'):
            instance.identified_by = None  # Se o checkbox estiver marcado, deixa anônimo
        else:
            instance.identified_by = self.user  # Caso contrário, atribui o usuário autenticado
        if commit:
            instance.save()
        return instance