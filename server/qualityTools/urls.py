from django.urls import path, include
from rest_framework.routers import DefaultRouter
from qualityTools.views.views_5w2h import (
    Ferramenta5W2HListView,
    Ferramenta5W2HCreateView,
    Ferramenta5W2HUpdateView,
    Ferramenta5W2HDeleteView,
)
from qualityTools.views.views_ishikawa import (
    FerramentaIshikawaListView,
    FerramentaIshikawaCreateView,
    FerramentaIshikawaUpdateView,
    FerramentaIshikawaDeleteView,
)
from qualityTools.views.views_swot import (
    FerramentaSWOTListView,
    FerramentaSWOTCreateView,
    FerramentaSWOTUpdateView,
    FerramentaSWOTDeleteView,
    FerramentaSWOTViewSet,
)
from qualityTools.views.views_5Porques import (
    Ferramenta5PorquesListView,
    Ferramenta5PorquesCreateView,
    Ferramenta5PorquesUpdateView,
    Ferramenta5PorquesDeleteView,
    Ferramenta5PorquesViewSet,
)

from qualityTools.views.views_sipoc import (
    FerramentaSIPOCListView,
    FerramentaSIPOCCreateView,
    FerramentaSIPOCUpdateView,
    FerramentaSIPOCDeleteView,
)

# Views da API usando Django REST Framework
from qualityTools.views.views_5w2h import Ferramenta5W2HViewSet
from qualityTools.views.views_ishikawa import FerramentaIshikawaViewSet
from qualityTools.views.views_swot import FerramentaSWOTViewSet
from qualityTools.views.views_5Porques import Ferramenta5PorquesViewSet

# Configurando o roteador para as views da API
router = DefaultRouter()
router.register(r'ferramenta-5w2h', Ferramenta5W2HViewSet)
router.register(r'ferramenta-ishikawa', FerramentaIshikawaViewSet)
router.register(r'ferramenta-swot', FerramentaSWOTViewSet)
router.register(r'ferramenta-5porques', Ferramenta5PorquesViewSet)

app_name = 'qualityTools'

urlpatterns = [
    # URLs para as views baseadas em classes do Django
    path('5w2h/', Ferramenta5W2HListView.as_view(), name='ferramenta5w2h_list'),
    path('5w2h/cadastrar/', Ferramenta5W2HCreateView.as_view(), name='ferramenta5w2h-create'),
    path('5w2h/editar/<int:pk>/', Ferramenta5W2HUpdateView.as_view(), name='ferramenta5w2h-update'),
    path('5w2h/deletar/<int:pk>/', Ferramenta5W2HDeleteView.as_view(), name='ferramenta5w2h-delete'),
    
    path('ishikawa/', FerramentaIshikawaListView.as_view(), name='ferramentaishikawa_list'),
    path('ishikawa/cadastrar/', FerramentaIshikawaCreateView.as_view(), name='ferramentaishikawa-create'),
    path('ishikawa/editar/<int:pk>/', FerramentaIshikawaUpdateView.as_view(), name='ferramentaishikawa-update'),
    path('ishikawa/deletar/<int:pk>/', FerramentaIshikawaDeleteView.as_view(), name='ferramentaishikawa-delete'),

    path('swot/', FerramentaSWOTListView.as_view(), name='ferramentaswot_list'),
    path('swot/cadastrar/', FerramentaSWOTCreateView.as_view(), name='ferramentaswot-create'),
    path('swot/editar/<int:pk>/', FerramentaSWOTUpdateView.as_view(), name='ferramentaswot-update'),
    path('swot/deletar/<int:pk>/', FerramentaSWOTDeleteView.as_view(), name='ferramentaswot-delete'),

    path('5-porques/', Ferramenta5PorquesListView.as_view(), name='ferramenta5porques_list'),
    path('5-porques/cadastrar/', Ferramenta5PorquesCreateView.as_view(), name='ferramenta5porques-create'),
    path('5-porques/editar/<int:pk>/', Ferramenta5PorquesUpdateView.as_view(), name='ferramenta5porques-update'),
    path('5-porques/deletar/<int:pk>/', Ferramenta5PorquesDeleteView.as_view(), name='ferramenta5porques-delete'),

    # FerramentaSIPOC URLs
    path('ferramenta-sipoc/', FerramentaSIPOCListView.as_view(), name='ferramentasipoc_list'),
    path('ferramenta-sipoc/create/', FerramentaSIPOCCreateView.as_view(), name='ferramentasipoc_create'),
    path('ferramenta-sipoc/update/<int:pk>/', FerramentaSIPOCUpdateView.as_view(), name='ferramentasipoc_update'),
    path('ferramenta-sipoc/delete/<int:pk>/', FerramentaSIPOCDeleteView.as_view(), name='ferramentasipoc_delete'),

    
    # Incluindo as rotas da API
    path('api/', include(router.urls)),
]
