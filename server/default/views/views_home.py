from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from default.models.models_links import Tool, AppsTool

@login_required
def home_view(request):
    tools = Tool.objects.all()
    apps = AppsTool.objects.all()
    user = request.user

    is_gestor = False

    if request.user.is_authenticated:
        is_gestor = request.user.grupos_set.filter(gestor=True).exists()

    return render(request, 'home/home.html', {
        'is_gestor': is_gestor,
        'tools': tools,
        'apps': apps,
        'user': user
    })
