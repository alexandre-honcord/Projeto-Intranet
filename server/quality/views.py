from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Opportunity, Notification
from .forms import OpportunityForm, NotificationForm
from rest_framework import viewsets
from .serializers import OpportunitySerializer, NotificationSerializer
from default.models.models_links import Tool, AppsTool

class OpportunityListView(ListView):
    model = Opportunity
    template_name = 'opportunity_list.html'
    context_object_name = 'opportunities'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()
        context['apps'] = AppsTool.objects.all()
        return context

class OpportunityDetailView(DetailView):
    model = Opportunity
    template_name = 'opportunity_detail.html'
    context_object_name = 'opportunity'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()
        context['apps'] = AppsTool.objects.all()
        return context

class OpportunityCreateView(CreateView):
    model = Opportunity
    form_class = OpportunityForm
    template_name = 'opportunity_form.html'
    success_url = reverse_lazy('quality:notification_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()
        context['apps'] = AppsTool.objects.all()
        return context

class OpportunityUpdateView(UpdateView):
    model = Opportunity
    form_class = OpportunityForm
    template_name = 'opportunity_form.html'
    success_url = reverse_lazy('quality:notification_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()
        context['apps'] = AppsTool.objects.all()
        return context

class OpportunityDeleteView(DeleteView):
    model = Opportunity
    template_name = 'opportunity_confirm_delete.html'
    success_url = reverse_lazy('quality:opportunity_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()
        context['apps'] = AppsTool.objects.all()
        return context

class OpportunityViewSet(viewsets.ModelViewSet):
    queryset = Opportunity.objects.all()
    serializer_class = OpportunitySerializer

class NotificationListView(ListView):
    model = Notification
    template_name = 'notification_list.html'
    context_object_name = 'notifications'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()
        context['apps'] = AppsTool.objects.all()
        return context

class NotificationDetailView(DetailView):
    model = Notification
    template_name = 'notification_detail.html'
    context_object_name = 'notification'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()
        context['apps'] = AppsTool.objects.all()
        return context

class NotificationCreateView(CreateView):
    model = Notification
    form_class = NotificationForm
    template_name = 'notification_form.html'
    success_url = reverse_lazy('quality:notification_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()
        context['apps'] = AppsTool.objects.all()
        return context

    def form_valid(self, form):
        if form.cleaned_data['identified_by'] == '':
            form.instance.identified_by = None
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

class NotificationUpdateView(UpdateView):
    model = Notification
    form_class = NotificationForm
    template_name = 'notification_form.html'
    success_url = reverse_lazy('quality:notification_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()
        context['apps'] = AppsTool.objects.all()
        return context

class NotificationDeleteView(DeleteView):
    model = Notification
    template_name = 'notification_confirm_delete.html'
    success_url = reverse_lazy('quality:notification_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tools'] = Tool.objects.all()
        context['apps'] = AppsTool.objects.all()
        return context

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
