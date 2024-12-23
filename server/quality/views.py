from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Opportunity, Notification
from .forms import OpportunityForm, NotificationForm
from rest_framework import viewsets
from .serializers import OpportunitySerializer, NotificationSerializer
from default.models.models_links import Tool, AppsTool
from django.contrib import messages

class BaseContextView:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()
        context['apps'] = AppsTool.objects.all()
        return context

class OpportunityListView(BaseContextView, ListView):
    model = Opportunity
    template_name = 'opportunity_list.html'
    context_object_name = 'opportunities'

    def get_queryset(self):
        # Ordena as notificações da mais nova para a mais antiga
        return Opportunity.objects.all().order_by('-created_at')

class OpportunityDetailView(BaseContextView, DetailView):
    model = Opportunity
    template_name = 'opportunity_detail.html'
    context_object_name = 'opportunity'

class OpportunityCreateView(BaseContextView, CreateView):
    model = Opportunity
    form_class = OpportunityForm
    template_name = 'opportunity_form.html'
    success_url = reverse_lazy('quality:opportunity_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Pass the authenticated user to the form
        return kwargs

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Oportunidade criada com sucesso!')  # Adiciona a mensagem de sucesso
        return response

class OpportunityUpdateView(BaseContextView, UpdateView):
    model = Opportunity
    form_class = OpportunityForm
    template_name = 'opportunity_form.html'
    success_url = reverse_lazy('quality:opportunity_list')

    def get_form_kwargs(self):
        # Adiciona o user nos kwargs do formulário
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Passa o usuário autenticado
        return kwargs

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Oportunidade atualizada com sucesso!')  # Adiciona a mensagem de sucesso
        return response

class OpportunityDeleteView(BaseContextView, DeleteView):
    model = Opportunity
    template_name = 'opportunity_confirm_delete.html'
    success_url = reverse_lazy('quality:opportunity_list')

class OpportunityViewSet(viewsets.ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = NotificationSerializer

class NotificationListView(BaseContextView, ListView):
    model = Notification
    template_name = 'notification_list.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        # Ordena as notificações da mais nova para a mais antiga
        return Notification.objects.all().order_by('-created_at')

class NotificationDetailView(BaseContextView, DetailView):
    model = Notification
    template_name = 'notification_detail.html'
    context_object_name = 'notification'

class NotificationCreateView(BaseContextView, CreateView):
    model = Notification
    form_class = NotificationForm
    template_name = 'notification_form.html'
    success_url = reverse_lazy('quality:notification_create')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Passa o usuário autenticado
        return kwargs

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Notificação criada com sucesso!')  # Adiciona a mensagem de sucesso
        return response

class NotificationUpdateView(BaseContextView, UpdateView):
    model = Notification
    form_class = NotificationForm
    template_name = 'notification_form.html'
    success_url = reverse_lazy('quality:notification_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user  # Passa o usuário autenticado
        return kwargs
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, 'Notificação atualizada com sucesso!')  # Adiciona a mensagem de sucesso
        return response

class NotificationDeleteView(BaseContextView, DeleteView):
    model = Notification
    template_name = 'notification_confirm_delete.html'
    success_url = reverse_lazy('quality:notification_list')

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

