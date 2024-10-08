from qualityTools.models.models_swot import FerramentaSWOT
from django.urls import reverse_lazy
from qualityTools.forms.forms_swot import FerramentaSWOTForm
from rest_framework import viewsets
from qualityTools.serializers.serializers_swot import FerramentaSWOTSerializer
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from default.models.models_links import Tool, AppsTool

class BaseContextView:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()
        context['apps'] = AppsTool.objects.all()
        return context

class FerramentaSWOTListView(BaseContextView, ListView):
    model = FerramentaSWOT
    template_name = 'ferramentas/ferramenta_swot/ferramenta_swot_list.html'
    context_object_name = 'ferramentas_swot'

class FerramentaSWOTCreateView(BaseContextView, CreateView):
    model = FerramentaSWOT
    template_name = 'ferramentas/ferramenta_swot/ferramenta_swot_form.html'
    form_class = FerramentaSWOTForm
    success_url = reverse_lazy('qualityTools:ferramentaswot_list')

class FerramentaSWOTUpdateView(BaseContextView, UpdateView):
    model = FerramentaSWOT
    template_name = 'ferramentas/ferramenta_swot/ferramenta_swot_form.html'
    form_class = FerramentaSWOTForm
    success_url = reverse_lazy('qualityTools:ferramentaswot_list')

class FerramentaSWOTDeleteView(BaseContextView, DeleteView):
    model = FerramentaSWOT
    template_name = 'ferramentas/ferramenta_swot/ferramenta_swot_confirm_delete.html'
    success_url = reverse_lazy('qualityTools:ferramentaswot_list')

class FerramentaSWOTViewSet(BaseContextView, viewsets.ModelViewSet):
    queryset = FerramentaSWOT.objects.all()
    serializer_class = FerramentaSWOTSerializer