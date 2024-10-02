from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from default.models.models_links import Tool, AppsTool
import time

@login_required
def home_view(request):
    tools = Tool.objects.all()
    apps = AppsTool.objects.all()
    user = request.user

    return render(request, 'home/home.html', {
        'tools': tools,
        'apps': apps,
        'user': user
    })
