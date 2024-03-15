from .models import *
from rest_framework import serializers

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        exclude = ['created_on','updated_on']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        exclude = ['created_on','updated_on']

class EventSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Events
        exclude = ['event_name']

class EventSpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSpeaker
        fields = ['speaker_name', 'speaker_desc']

class EventDetailSerializer(serializers.ModelSerializer):
    event_speakers = EventSpeakerSerializer(many=True)

    class Meta:
        model = Events
        fields = ['id', 'event_name', 'event_title', 'event_date', 'event_time', 'event_location', 'event_desc', 'event_image', 'event_videos', 'event_speakers']

class EventSpeakersCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSpeaker
        fields = '__all__'

