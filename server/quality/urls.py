# core/urls.py
from django.urls import path,include
from . import views
# from rest_framework.routers import DefaultRouter
from .views import NotificationViewSet,OpportunityViewSet

# Configurando o roteador para as views da API
# router = DefaultRouter()
# router.register(r'opportunities-api', OpportunityViewSet)
# router.register(r'notifications-api', NotificationViewSet)

app_name = 'quality'

urlpatterns = [
    path('opportunities/', views.OpportunityListView.as_view(), name='opportunity_list'),
    path('opportunities/<int:pk>/', views.OpportunityDetailView.as_view(), name='opportunity_detail'),
    path('opportunities/create/', views.OpportunityCreateView.as_view(), name='opportunity_create'),
    path('opportunities/<int:pk>/update/', views.OpportunityUpdateView.as_view(), name='opportunity_update'),
    path('opportunities/<int:pk>/delete/', views.OpportunityDeleteView.as_view(), name='opportunity_delete'),

    path('notifications/', views.NotificationListView.as_view(), name='notification_list'),
    path('notifications/<int:pk>/', views.NotificationDetailView.as_view(), name='notification_detail'),
    path('notifications/create/', views.NotificationCreateView.as_view(), name='notification_create'),
    path('notifications/<int:pk>/update/', views.NotificationUpdateView.as_view(), name='notification_update'),
    path('notifications/<int:pk>/delete/', views.NotificationDeleteView.as_view(), name='notification_delete'),
]
