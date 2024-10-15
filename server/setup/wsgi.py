import os
import sys

# Adiciona o diretório do projeto ao sys.path
sys.path.append('/home/user/Projeto-Intranet/server')

# Define o módulo de configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')

from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
