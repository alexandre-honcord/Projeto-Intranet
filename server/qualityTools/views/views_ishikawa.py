from qualityTools.models.models_ishikawa import FerramentaIshikawa
from django.urls import reverse_lazy
from qualityTools.forms.forms_ishikawa import FerramentaIshikawaForm
from rest_framework import viewsets
from qualityTools.serializers.serializers_ishikawa import FerramentaIshikawaSerializer
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

class FerramentaIshikawaListView(ListView):
    model = FerramentaIshikawa
    template_name = 'ferramentas/ferramentaishikawa/ferramentaishikawa_list.html'
    context_object_name = 'ferramentas_ishikawa'

class FerramentaIshikawaCreateView(CreateView):
    model = FerramentaIshikawa
    form_class = FerramentaIshikawaForm
    template_name = 'ferramentas/ferramentaishikawa/ferramentaishikawa_form.html'
    success_url = reverse_lazy('ferramentaishikawa_list')

class FerramentaIshikawaUpdateView(UpdateView):
    model = FerramentaIshikawa
    form_class = FerramentaIshikawaForm
    template_name = 'ferramentas/ferramentaishikawa/ferramentaishikawa_form.html'
    success_url = reverse_lazy('ferramentaishikawa_list')

class FerramentaIshikawaDeleteView(DeleteView):
    model = FerramentaIshikawa
    template_name = 'ferramentas/ferramentaishikawa/ferramentaishikawa_confirm_delete.html'
    success_url = reverse_lazy('ferramentaishikawa_list')

class FerramentaIshikawaViewSet(viewsets.ModelViewSet):
    queryset = FerramentaIshikawa.objects.all()
    serializer_class = FerramentaIshikawaSerializer