from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from qualityTools.models.models_5Porques import Ferramenta5Porques
from qualityTools.forms.forms_5Porques import Ferramenta5PorquesForm
from qualityTools.serializers.serializers_5Porques import Ferramenta5PorquesSerializer
from default.models.models_links import Tool, AppsTool

class BaseContextView:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()
        context['apps'] = AppsTool.objects.all()
        return context

class Ferramenta5PorquesListView(BaseContextView, ListView):
    model = Ferramenta5Porques
    template_name = 'ferramentas/ferramenta5Porques/ferramenta5Porques_list.html'
    context_object_name = 'ferramentas_5porques'

class Ferramenta5PorquesCreateView(BaseContextView, CreateView):
    model = Ferramenta5Porques
    template_name = 'ferramentas/ferramenta5Porques/ferramenta5Porques_form.html'
    form_class = Ferramenta5PorquesForm
    success_url = reverse_lazy('qualityTools:ferramenta5porques_list')

class Ferramenta5PorquesUpdateView(BaseContextView, UpdateView):
    model = Ferramenta5Porques
    template_name = 'ferramentas/ferramenta5Porques/ferramenta5Porques_form.html'
    form_class = Ferramenta5PorquesForm
    success_url = reverse_lazy('qualityTools:ferramenta5porques_list')

class Ferramenta5PorquesDeleteView(BaseContextView, DeleteView):
    model = Ferramenta5Porques
    template_name = 'ferramentas/ferramenta5Porques/ferramenta5Porques_confirm_delete.html'
    context_object_name = 'ferramenta'  # Define o nome do objeto no template
    success_url = reverse_lazy('qualityTools:ferramenta5porques_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ferramenta'] = self.get_object()  # Passa o objeto para o template
        return context

class Ferramenta5PorquesViewSet(BaseContextView, viewsets.ModelViewSet):
    queryset = Ferramenta5Porques.objects.all()
    serializer_class = Ferramenta5PorquesSerializer
