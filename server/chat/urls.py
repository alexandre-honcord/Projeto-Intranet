from django.urls import path
from . import views

app_name='chat'
urlpatterns = [
    path('', views.home, name="home"),
    path('create-room/', views.create_room, name="create_room"),
    path('<int:pk>/', views.RoomDetailView.as_view(), name="room_detail"),
    path('<int:pk>/send/', views.send_message, name="send_message"),
]