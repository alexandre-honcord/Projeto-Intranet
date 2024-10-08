# qualityTools/admin.py
from django.contrib import admin
from qualityTools.models.models_5w2h import Ferramenta5W2H
from qualityTools.models.models_ishikawa import FerramentaIshikawa
from qualityTools.models.models_swot import FerramentaSWOT
from qualityTools.models.models_5Porques import Ferramenta5Porques

admin.site.register(Ferramenta5W2H)
admin.site.register(FerramentaIshikawa)
admin.site.register(FerramentaSWOT)
admin.site.register(Ferramenta5Porques)
