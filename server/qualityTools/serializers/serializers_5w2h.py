from rest_framework import serializers
from qualityTools.models.models_5w2h import Ferramenta5W2H

class Ferramenta5W2HSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ferramenta5W2H
        fields = '__all__'