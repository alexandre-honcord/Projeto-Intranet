from django.contrib import admin

from default.models.models_tasy import User
from default.models.models_links import Tool, AppsTool

admin.site.register(Tool)
admin.site.register(AppsTool)
admin.site.register(User)
