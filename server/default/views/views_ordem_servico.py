from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from default.models.models_links import Tool, AppsTool
import time

@login_required
def ordemServico_view(request):
    tools = Tool.objects.all()
    apps = AppsTool.objects.all()
    user = request.user

    return render(request, 'ordemServico/ordemServico.html', {
        'tools': tools,
        'apps': apps,
        'user': user
    })


def painelOrdemServico_view(request):
    tools = Tool.objects.all()
    apps = AppsTool.objects.all()
    user = request.user

    return render(request, 'ordemServico/painelOrdemServico.html', {
        'tools': tools,
        'apps': apps,
        'user': user
    })