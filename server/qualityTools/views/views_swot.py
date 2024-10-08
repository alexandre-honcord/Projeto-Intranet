from qualityTools.models.models_swot import FerramentaSWOT
from django.urls import reverse_lazy
from qualityTools.forms.forms_swot import FerramentaSWOTForm
from rest_framework import viewsets
from qualityTools.serializers.serializers_swot import FerramentaSWOTSerializer
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class FerramentaSWOTListView(ListView):
    model = FerramentaSWOT
    template_name = 'ferramentas/ferramenta_swot/ferramenta_swot_list.html'
    context_object_name = 'ferramentas_swot'

class FerramentaSWOTCreateView(CreateView):
    model = FerramentaSWOT
    template_name = 'ferramentas/ferramenta_swot/ferramenta_swot_form.html'
    fields = ['oportunidade_melhoria', 'notificacao_evento_adverso', 'forcas', 'fraquezas', 'oportunidades', 'ameacas']
    success_url = reverse_lazy('qualityTools:ferramentaswot_list')

class FerramentaSWOTUpdateView(UpdateView):
    model = FerramentaSWOT
    template_name = 'ferramentas/ferramenta_swot/ferramenta_swot_form.html'
    fields = ['oportunidade_melhoria', 'notificacao_evento_adverso', 'forcas', 'fraquezas', 'oportunidades', 'ameacas']
    success_url = reverse_lazy('qualityTools:ferramentaswot_list')

class FerramentaSWOTDeleteView(DeleteView):
    model = FerramentaSWOT
    template_name = 'ferramentas/ferramenta_swot/ferramenta_swot_confirm_delete.html'
    success_url = reverse_lazy('qualityTools:ferramentaswot_list')

class FerramentaSWOTViewSet(viewsets.ModelViewSet):
    queryset = FerramentaSWOT.objects.all()
    serializer_class = FerramentaSWOTSerializer