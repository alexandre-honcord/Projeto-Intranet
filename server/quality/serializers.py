from rest_framework import serializers
from .models import Opportunity, Notification

class OpportunitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Opportunity

        fields = '__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = '__all__'
