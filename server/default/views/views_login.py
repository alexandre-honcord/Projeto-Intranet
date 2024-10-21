from django.contrib.auth import login as django_login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from default.models.models_links import Tool
from default.utils import exists_ad
from default.utils import buscar_foto_usuario
import logging
from django.utils import timezone

logger = logging.getLogger(__name__)

@csrf_protect
def login_view(request):
    tools = Tool.objects.all()

    if request.user.is_authenticated:
        return redirect(reverse('intra:home'))

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar usuário com LDAP
        ldap_user = exists_ad(username, password)

        if ldap_user is not None:
            django_user, created = User.objects.get_or_create(username=username)

            if created:
                logger.info(f'User {username} created in Django database.')

            # Atualiza o último login
            django_user.last_login = timezone.now()
            django_user.save()

            # Buscar a foto e converter para base64
            foto_base64 = buscar_foto_usuario(username)
            
            # Armazenar a foto na sessão
            if foto_base64:
                request.session['foto_usuario'] = foto_base64

            # Faz o login do usuário
            django_login(request, django_user)

            # Redireciona para a URL configurada
            return redirect(reverse('intra:home'))
        else:
            return render(request, 'login/login.html', {
                'error_message': 'Credenciais inválidas. Por favor, tente novamente.',
                'tools': tools
            })
    else:
        return render(request, 'login/login.html', {'tools': tools})


def logout_view(request):
    logout(request)  # Desloga o usuário
    return redirect(reverse('intra:login'))  # Redireciona para a página de login