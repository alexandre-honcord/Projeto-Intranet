from rest_framework import serializers
from qualityTools.models.models_ishikawa import FerramentaIshikawa

class FerramentaIshikawaSerializer(serializers.ModelSerializer):
    class Meta:
        model = FerramentaIshikawa
        fields = '__all__'