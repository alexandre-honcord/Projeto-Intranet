from rest_framework import serializers
from qualityTools.models.models_5Porques import Ferramenta5Porques

class Ferramenta5PorquesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ferramenta5Porques
        fields = '__all__'