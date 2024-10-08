from rest_framework import serializers
from qualityTools.models.models_swot import FerramentaSWOT


class FerramentaSWOTSerializer(serializers.ModelSerializer):
    class Meta:
        model = FerramentaSWOT
        fields = '__all__'