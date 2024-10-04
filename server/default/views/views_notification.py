from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from default.models.models_links import Tool, AppsTool


@login_required
def notification_view(request):
    tools = Tool.objects.all()
    apps = AppsTool.objects.all()
    user = request.user

    return render(request, 'notification/notification.html', {
        'tools': tools,
        'apps': apps,
        'user': user
    })