from django.urls import path
from default.views.views_index import index
from default.views.views_login import login_view, logout_view
from default.views.views_home import home_view
from default.views.views_ordem_servico import ordemServico_view, ordemServicoClass_view



app_name = 'intra'

urlpatterns = [
    path('index/', index, name='index'),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('home/', home_view, name='home'),
    path('ordemServico/', ordemServico_view, name='ordemServico'),
    path('ordemServicoClass/', ordemServicoClass_view, name='ordemServicoClass'),

]
