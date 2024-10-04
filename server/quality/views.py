# core/views.py
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Opportunity, Notification
from .forms import OpportunityForm, NotificationForm
from rest_framework import viewsets
from .serializers import OpportunitySerializer,NotificationSerializer


class OpportunityListView(ListView):
    model = Opportunity
    template_name = 'opportunity_list.html'
    context_object_name = 'opportunities'

class OpportunityDetailView(DetailView):
    model = Opportunity
    template_name = 'opportunity_detail.html'
    context_object_name = 'opportunities'

class OpportunityCreateView(CreateView):
    model = Opportunity
    form_class = OpportunityForm
    template_name = 'opportunity_form.html'
    success_url = reverse_lazy('quality:notification_list')


class OpportunityUpdateView(UpdateView):
    model = Opportunity
    form_class = OpportunityForm
    template_name = 'opportunity_form.html'
    success_url = reverse_lazy('quality:notification_list')

class OpportunityDeleteView(DeleteView):
    model = Opportunity
    template_name = 'opportunity_confirm_delete.html'
    success_url = reverse_lazy('quality:opportunity_list')

class OpportunityViewSet(viewsets.ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer

class NotificationListView(ListView):
    model = Notification
    template_name = 'notification_list.html'
    context_object_name = 'notifications'

class NotificationDetailView(DetailView):
    model = Notification
    template_name = 'notification_detail.html'
    context_object_name = 'notification'

class NotificationCreateView(CreateView):
    model = Notification
    form_class = NotificationForm
    template_name = 'notification_form.html'
    success_url = reverse_lazy('quality:notification_list')

    def form_valid(self, form):
        print("Form is valid.")
        print("Cleaned data:", form.cleaned_data)  # Logando os dados que passaram pela validação

        if form.cleaned_data['identified_by'] == '':
            print("Identified by is empty, setting it to None.")  # Log caso o campo 'identified_by' esteja vazio
            form.instance.identified_by = None

        response = super().form_valid(form)
        print("Notification created successfully, redirecting...")  # Log após o objeto ser salvo com sucesso
        return response

    def form_invalid(self, form):
        print("Form is invalid.")
        print("Errors:", form.errors)  # Logando os erros que ocorreram durante a validação do formulário
        return self.render_to_response(self.get_context_data(form=form))

class NotificationUpdateView(UpdateView):
    model = Notification
    form_class = NotificationForm
    template_name = 'notification_form.html'
    success_url = reverse_lazy('quality:notification_list')

class NotificationDeleteView(DeleteView):
    model = Notification
    template_name = 'notification_confirm_delete.html'
    success_url = reverse_lazy('quality:notification_list')

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
