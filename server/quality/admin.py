from django.contrib import admin
from .models import Opportunity, Notification,Status, Location, Client, Grupos

admin.site.register(Opportunity)
admin.site.register(Notification)
admin.site.register(Status)
admin.site.register(Location)
admin.site.register(Client)

class GruposAdmin(admin.ModelAdmin):
    list_display = ('user', 'gestor')  # Campos a serem exibidos na lista
    list_filter = ('gestor',)  # Filtro para o campo 'gestor'
    search_fields = ('user__username', 'user__first_name')  # Pesquisa por username e nome do usuário

    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.select_related('user')  # Otimiza a consulta para evitar N+1

admin.site.register(Grupos, GruposAdmin)
