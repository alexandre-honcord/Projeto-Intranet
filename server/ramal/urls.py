# ramal/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('ramais/', views.lista_ramais, name='lista_ramais'),
    path('ajax/ramais/', views.ajax_lista_ramais, name='ajax_lista_ramais'),
]
