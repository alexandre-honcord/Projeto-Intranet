from django.contrib import admin
from .models import Opportunity, Notification,Status, Location, Client

admin.site.register(Opportunity)
admin.site.register(Notification)
admin.site.register(Status)
admin.site.register(Location)
admin.site.register(Client)
