from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from qualityTools.forms.forms_sipoc import FerramentaSIPOCForm, MapeamentoSIPOCForm
from qualityTools.models.models_sipoc import FerramentaSIPOC, MapeamentoSIPOC
from default.models.models_links import Tool, AppsTool

class BaseContextView:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()
        context['apps'] = AppsTool.objects.all()
        return context

class FerramentaSIPOCListView(BaseContextView, ListView):
    model = FerramentaSIPOC
    template_name = 'ferramentas/ferramenta_sipoc/ferramenta_sipoc_list.html'
    context_object_name = 'ferramentas_sipoc'

    def get_queryset(self):
        # Retornar FerramentaSIPOC com dados do MapeamentoSIPOC relacionados
        return FerramentaSIPOC.objects.select_related('mapeamento')

# Create View for FerramentaSIPOC
class FerramentaSIPOCCreateView(CreateView):
    model = FerramentaSIPOC
    template_name = 'ferramentas/ferramenta_sipoc/ferramenta_sipoc_form.html'
    form_class = FerramentaSIPOCForm
    success_url = reverse_lazy('qualityTools:ferramentasipoc_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.POST:
            context['mapeamento_form'] = MapeamentoSIPOCForm(self.request.POST)
        else:
            context['mapeamento_form'] = MapeamentoSIPOCForm()
        return context

    def form_valid(self, form):
        mapeamento_form = MapeamentoSIPOCForm(self.request.POST)
        if mapeamento_form.is_valid():
            mapeamento = mapeamento_form.save()  # Salva o mapeamento corretamente
            form.instance.mapeamento = mapeamento  # Associa o mapeamento ao FerramentaSIPOC
            return super().form_valid(form)
        else:
            return self.form_invalid(form)

# Update View for FerramentaSIPOC
class FerramentaSIPOCUpdateView(BaseContextView, UpdateView):
    model = FerramentaSIPOC
    template_name = 'ferramentas/ferramenta_sipoc/ferramenta_sipoc_form.html'
    form_class = FerramentaSIPOCForm
    success_url = reverse_lazy('qualityTools:ferramentasipoc_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mapeamento_form'] = MapeamentoSIPOCForm(instance=self.object.mapeamento)
        return context

# Delete View for FerramentaSIPOC
class FerramentaSIPOCDeleteView(BaseContextView, DeleteView):
    model = FerramentaSIPOC
    template_name = 'ferramentas/ferramenta_sipoc/ferramenta_sipoc_confirm_delete.html'
    success_url = reverse_lazy('qualityTools:ferramentasipoc_list')
