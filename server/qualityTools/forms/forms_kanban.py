from django import forms
from qualityTools.models.models_kanban import Board, Column, Card

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['name', 'description']

class ColumnForm(forms.ModelForm):
    class Meta:
        model = Column
        fields = ['board', 'name', 'order']

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = ['column', 'title', 'description', 'order']