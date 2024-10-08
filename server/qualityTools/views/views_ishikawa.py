from qualityTools.models.models_ishikawa import FerramentaIshikawa
from django.urls import reverse_lazy
from qualityTools.forms.forms_ishikawa import FerramentaIshikawaForm
from rest_framework import viewsets
from qualityTools.serializers.serializers_ishikawa import FerramentaIshikawaSerializer
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from default.models.models_links import Tool, AppsTool

class BaseContextView:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()
        context['apps'] = AppsTool.objects.all()
        return context

class FerramentaIshikawaListView(BaseContextView, ListView):
    model = FerramentaIshikawa
    template_name = 'ferramentas/ferramentaishikawa/ferramentaishikawa_list.html'
    context_object_name = 'ferramentas_ishikawa'

class FerramentaIshikawaCreateView(BaseContextView, CreateView):
    model = FerramentaIshikawa
    form_class = FerramentaIshikawaForm
    template_name = 'ferramentas/ferramentaishikawa/ferramentaishikawa_form.html'
    success_url = reverse_lazy('qualityTools:ferramentaishikawa_list')

class FerramentaIshikawaUpdateView(BaseContextView, UpdateView):
    model = FerramentaIshikawa
    form_class = FerramentaIshikawaForm
    template_name = 'ferramentas/ferramentaishikawa/ferramentaishikawa_form.html'
    success_url = reverse_lazy('qualityTools:ferramentaishikawa_list')

class FerramentaIshikawaDeleteView(BaseContextView, DeleteView):
    model = FerramentaIshikawa
    template_name = 'ferramentas/ferramentaishikawa/ferramentaishikawa_confirm_delete.html'
    context_object_name = 'ferramenta'  # Define o nome do objeto no template
    success_url = reverse_lazy('qualityTools:ferramentaishikawa_list')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ferramenta'] = self.get_object()  # Passa o objeto para o template
        return context

class FerramentaIshikawaViewSet(BaseContextView, viewsets.ModelViewSet):
    queryset = FerramentaIshikawa.objects.all()
    serializer_class = FerramentaIshikawaSerializer