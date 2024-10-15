import json
from django.shortcuts import render
from .models import Message, Room
from django.views.generic.detail import DetailView
from django.http import JsonResponse
from default.models.models_links import Tool, AppsTool

def get_common_context():
    return {
        'tools': Tool.objects.all(),
        'apps': AppsTool.objects.all()
    }

def home(request):
    rooms = Room.objects.all().order_by('-created_at')
    context = {
        'rooms': rooms,
    }
    context.update(get_common_context())  # Adiciona o contexto comum
    return render(request, 'chat/home.html', context)

class RoomDetailView(DetailView):
    model = Room
    template_name = 'chat/list-messages.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def send_message(request, pk):
    if request.method == "POST":
        data = json.loads(request.body)
        room = Room.objects.get(id=pk)
        new_message = Message.objects.create(user=request.user, room=room, text=data['message'])
        context = {
            'm': new_message,
        }
        context.update(get_common_context())  # Adiciona o contexto comum
        return render(request, 'chat/message.html', context)
    return JsonResponse({'error': 'Método não permitido'}, status=405)

def create_room(request):
    if request.method == "POST":
        data = json.loads(request.body)
        room = Room.objects.create(user=request.user, title=data['title'])
        context = {
            'r': room,
        }
        context.update(get_common_context())  # Adiciona o contexto comum
        return render(request, 'chat/room.html', context)
    return JsonResponse({'error': 'Método não permitido'}, status=405)