from django.urls import path
from default.views.views_index import index
from default.views.views_login import login_view, logout_view, verificar_foto_view
from default.views.views_home import home_view
from default.views.views_ordem_servico import ordemServico_view, painelOrdemServico_view, processar_ordem_servico
from default.views.views_notification import   notification_view
from quality.views import OpportunityListView

app_name = 'intra'

urlpatterns = [
    path('index/', index, name='index'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('load/', verificar_foto_view, name='verificar_foto_usuario'),
    path('ordemServico/', ordemServico_view, name='ordemServico'),
    path('processar-ordem/', processar_ordem_servico, name='processar_ordem_servico'),
    path('notificacoes/', notification_view, name='notifications'),
    path('painel/OrdemServico', painelOrdemServico_view, name='painelOrdemServico'),
    path('quality/', OpportunityListView.as_view(), name='quality')
]
