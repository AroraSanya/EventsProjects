from rest_framework import serializers, status
from Events.models import *

class EventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields =('title',"description","start_datetime","end_datetime","address","event_at","events_status")

class JoineventsSerializer(serializers.ModelSerializer):
        class Meta:
            model = Join_events
            fields ='__all__'
class ReportSerializer(serializers.ModelSerializer):
     atendees=serializers.StringRelatedField(many=True)
     class Meta:
            model = Event
            fields ='__all__'