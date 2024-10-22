from django.contrib.auth import login as django_login, logout
from default.models.models_tasy import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.csrf import csrf_protect
from default.models.models_links import Tool
from default.utils import exists_ad
from default.utils import buscar_dados_usuario
import base64
from django.core.files.base import ContentFile 
import logging
from django.utils import timezone
from django.http import JsonResponse

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
            # Tenta obter ou criar o usuário no Django
            django_user, created = User.objects.get_or_create(username=username)

            # Se o usuário foi criado (login pela primeira vez)
            if created:
                dados_usuario = buscar_dados_usuario(username)

                if dados_usuario:
                    # Preencher os campos do modelo com os dados da consulta
                    django_user.IDtasy = dados_usuario['IDtasy']
                    django_user.name = dados_usuario['name']

                    # Salvar a foto como arquivo no modelo User, se houver foto
                    if dados_usuario.get('foto'):
                        foto_content = ContentFile(base64.b64decode(dados_usuario['foto']))
                        django_user.foto.save(f"{username}.jpg", foto_content, save=True)

                    # Atualiza o último login
                    django_user.last_login = timezone.now()
                    django_user.save()

                    # Armazenar a foto na sessão
                    request.session['foto_usuario'] = dados_usuario['foto']
                else:
                    # Se não houver dados, você pode querer lidar com isso de outra forma
                    logger.warning(f'No user data found for {username}.')

            else:
                # Se o usuário já existe, apenas atualiza o último login
                django_user.last_login = timezone.now()
                django_user.save()

            # Faz o login do usuário
            django_login(request, django_user)

            # Define uma variável de sessão para indicar que o login foi bem-sucedido
            request.session['login_success'] = True
            
            # Redireciona para a URL configurada
            return redirect(reverse('intra:home'))
        else:
            return render(request, 'login/login.html', {
                'error_message': 'Credenciais inválidas. Por favor, tente novamente.',
                'tools': tools
            })
    else:
        return render(request, 'login/login.html', {'tools': tools})

def verificar_foto_usuario(django_user):
    # Lógica para verificar a foto do usuário após o login
    dados_usuario = buscar_dados_usuario(django_user.username)  # Chama a função para buscar dados novamente

    if dados_usuario and dados_usuario['foto']:
        # Verifica se a foto do banco é diferente da já salva
        if (not django_user.foto or 
            not django_user.foto.name.endswith(dados_usuario['foto'].split('/')[-1])):
            # Salvar a nova foto como arquivo no modelo User
            foto_content = ContentFile(base64.b64decode(dados_usuario['foto']))
            django_user.foto.save(f"{django_user.username}_profile.jpg", foto_content, save=True)

def verificar_foto_view(request):
    if request.user.is_authenticated:
        verificar_foto_usuario(request.user)  # Chama sua função de verificação
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=403)


def logout_view(request):
    logout(request)  # Desloga o usuário
    return redirect(reverse('intra:login'))  # Redireciona para a página de login