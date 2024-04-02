from rest_framework.serializers import ModelSerializer, ValidationError
from .models import *
from rest_framework import serializers
from .models import *
from rest_framework import serializers

class EventSpeakersCardSerializer(serializers.ModelSerializer):
    event_id = serializers.PrimaryKeyRelatedField(source='event.id', read_only=True)

    class Meta:
        model = EventSpeaker
        fields = ['event_id', 'name', 'image', 'desc','id']

class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImages
        fields = ('id', 'image')

class EventSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Event
        fields = ["id", "school", "name" ,"title", "date", "time", "location", "desc",  "thumbnail", "videos", "images", "uploaded_images"]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        event = Event.objects.create(**validated_data)
        for image in uploaded_images:
            EventImages.objects.create(event=event, image=image)
        return event

class EventSerializer1(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ["id", "time", "title", "images", "location", "desc", "date"]


class EventDetailSerializer(serializers.ModelSerializer):
    # event_speakers = EventSpeakersCardSerializer(many=True)
    images = EventImageSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ['id', 'name', 'title', 'date', 'time', 
                'location', 'desc', 'images', 'videos']

