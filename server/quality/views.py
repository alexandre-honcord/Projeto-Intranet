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
    success_url = reverse_lazy('core:notification_list')


class OpportunityUpdateView(UpdateView):
    model = Opportunity
    form_class = OpportunityForm
    template_name = 'opportunity_form.html'
    success_url = reverse_lazy('core:notification_list')

class OpportunityDeleteView(DeleteView):
    model = Opportunity
    template_name = 'opportunity_confirm_delete.html'
    success_url = reverse_lazy('core:opportunity_list')

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
    success_url = reverse_lazy('core:notification_list')

    def form_valid(self, form):
        if form.cleaned_data['identified_by'] == '':
            form.instance.identified_by = None
        return super().form_valid(form)

class NotificationUpdateView(UpdateView):
    model = Notification
    form_class = NotificationForm
    template_name = 'notification_form.html'
    success_url = reverse_lazy('core:notification_list')

class NotificationDeleteView(DeleteView):
    model = Notification
    template_name = 'notification_confirm_delete.html'
    success_url = reverse_lazy('core:notification_list')

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
