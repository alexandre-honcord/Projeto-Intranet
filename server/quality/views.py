from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Opportunity, Notification
from .forms import OpportunityForm, NotificationForm
from rest_framework import viewsets
from .serializers import OpportunitySerializer, NotificationSerializer
from default.models.models_links import Tool, AppsTool

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

class OpportunityDetailView(BaseContextView, DetailView):
    model = Opportunity
    template_name = 'opportunity_detail.html'
    context_object_name = 'opportunity'

class OpportunityCreateView(BaseContextView, CreateView):
    model = Opportunity
    form_class = OpportunityForm
    template_name = 'opportunity_form.html'
    success_url = reverse_lazy('quality:notification_list')

class OpportunityUpdateView(BaseContextView, UpdateView):
    model = Opportunity
    form_class = OpportunityForm
    template_name = 'opportunity_form.html'
    success_url = reverse_lazy('quality:notification_list')

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

class NotificationDetailView(BaseContextView, DetailView):
    model = Notification
    template_name = 'notification_detail.html'
    context_object_name = 'notification'

class NotificationCreateView(BaseContextView, CreateView):
    model = Notification
    form_class = NotificationForm
    template_name = 'notification_form.html'
    success_url = reverse_lazy('quality:notification_list')

    def form_valid(self, form):
        if form.cleaned_data['identified_by'] == '':
            form.instance.identified_by = None
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class NotificationUpdateView(BaseContextView, UpdateView):
    model = Notification
    form_class = NotificationForm
    template_name = 'notification_form.html'
    success_url = reverse_lazy('quality:notification_list')

class NotificationDeleteView(BaseContextView, DeleteView):
    model = Notification
    template_name = 'notification_confirm_delete.html'
    success_url = reverse_lazy('quality:notification_list')

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

