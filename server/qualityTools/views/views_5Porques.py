from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from qualityTools.models.models_5Porques import Ferramenta5Porques
from qualityTools.forms.forms_5Porques import Ferramenta5PorquesForm
from qualityTools.serializers.serializers_5Porques import Ferramenta5PorquesSerializer

class Ferramenta5PorquesListView(ListView):
    model = Ferramenta5Porques
    template_name = 'ferramentas/ferramenta5Porques/ferramenta5Porques_list.html'
    context_object_name = 'ferramentas_5porques'

class Ferramenta5PorquesCreateView(CreateView):
    model = Ferramenta5Porques
    template_name = 'ferramentas/ferramenta5Porques/ferramenta5Porques_form.html'
    form_class = Ferramenta5PorquesForm
    success_url = reverse_lazy('ferramenta5porques_list')

class Ferramenta5PorquesUpdateView(UpdateView):
    model = Ferramenta5Porques
    template_name = 'ferramentas/ferramenta5Porques/ferramenta5Porques_form.html'
    form_class = Ferramenta5PorquesForm
    success_url = reverse_lazy('ferramenta5porques_list')

class Ferramenta5PorquesDeleteView(DeleteView):
    model = Ferramenta5Porques
    template_name = 'ferramentas/ferramenta5Porques/ferramenta5Porques_confirm_delete.html'
    success_url = reverse_lazy('ferramenta5porques_list')

class Ferramenta5PorquesViewSet(viewsets.ModelViewSet):
    queryset = Ferramenta5Porques.objects.all()
    serializer_class = Ferramenta5PorquesSerializer
