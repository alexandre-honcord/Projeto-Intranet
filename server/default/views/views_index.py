from django.shortcuts import render
from default.models.models_links import Tool

def index(request):
    tools = Tool.objects.all()
    return render(request, 'index/index.html', {'tools': tools,})