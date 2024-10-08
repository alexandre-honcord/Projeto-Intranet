from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets
from qualityTools.models.models_5w2h import Ferramenta5W2H
from qualityTools.forms.forms_5w2h import Ferramenta5W2HForm
from qualityTools.serializers.serializers_5w2h import Ferramenta5W2HSerializer
from default.models.models_links import Tool, AppsTool

class BaseContextView:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()
        context['apps'] = AppsTool.objects.all()
        return context

class Ferramenta5W2HListView(BaseContextView, ListView):
    model = Ferramenta5W2H
    template_name = 'ferramentas/ferramenta5w2h/ferramenta5w2h_list.html'
    context_object_name = 'ferramentas_5w2h'


class Ferramenta5W2HCreateView(BaseContextView, CreateView):
    model = Ferramenta5W2H
    form_class = Ferramenta5W2HForm
    template_name = 'ferramentas/ferramenta5w2h/ferramenta5w2h_form.html'
    success_url = reverse_lazy('qualityTools:ferramenta5w2h_list')


class Ferramenta5W2HUpdateView(BaseContextView, UpdateView):
    model = Ferramenta5W2H
    form_class = Ferramenta5W2HForm
    template_name = 'ferramentas/ferramenta5w2h/ferramenta5w2h_form.html'
    success_url = reverse_lazy('qualityTools:ferramenta5w2h_list')

    def form_valid(self, form):
        # Captura a opção selecionada
        if 'options' in self.request.POST:
            selected_option = self.request.POST['options']

            # Atribui o valor correto com base na opção selecionada
            if selected_option == 'True':
                # Salva oportunidade de melhoria
                form.instance.notificacao_evento_adverso = None  # Limpa notificação se estiver selecionada a oportunidade
            elif selected_option == 'False':
                # Salva notificação de evento adverso
                form.instance.oportunidade_melhoria = None  # Limpa oportunidade se estiver selecionada a notificação

        return super().form_valid(form)


class Ferramenta5W2HDeleteView(BaseContextView, DeleteView):
    model = Ferramenta5W2H
    template_name = 'ferramentas/ferramenta5w2h/ferramenta5w2h_confirm_delete.html'
    success_url = reverse_lazy('qualityTools:ferramenta5w2h_list')


class Ferramenta5W2HViewSet(BaseContextView, viewsets.ModelViewSet):
    queryset = Ferramenta5W2H.objects.all()
    serializer_class = Ferramenta5W2HSerializer
