import json
from django.shortcuts import render
from .models import Message, Room
from django.views.generic.detail import DetailView
from django.http import JsonResponse

def home(request):
    rooms = Room.objects.all().order_by('-created_at')
    return render(request, 'chat/home.html', {
        'rooms': rooms,
    })

class RoomDetailView(DetailView):
    model = Room
    template_name = 'chat/list-messages.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def send_message(request, pk):
    if request.method == "POST":
        data = json.loads(request.body)
        room = Room.objects.get(id=pk)  # Obtenha a sala pelo ID
        new_message = Message.objects.create(user=request.user, room=room, text=data['message'])  # Cria a nova mensagem
        return render(request, 'chat/message.html', {
            'm': new_message
        })
    return JsonResponse({'error': 'Método não permitido'}, status=405)

def create_room(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print("Dados recebidos:", data)  # Debugging
        room = Room.objects.create(user=request.user, title=data['title'])
        return render(request, 'chat/room.html', {
            'r': room
        })
    return JsonResponse({'error': 'Método não permitido'}, status=405)