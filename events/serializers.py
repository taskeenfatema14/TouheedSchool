
from rest_framework.serializers import ModelSerializer, ValidationError
from .models import *
from rest_framework import serializers

from .models import *
from rest_framework import serializers

############################################ EVENT IMAGE ########################################################

class EventImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImages
        fields = ["event", "image"]

############################################ EVENT ########################################################

############################################ EVENT ########################################################

class EventSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True
    )

    class Meta:
        model = Events

        # fields = ["id", "school", "event_name", "event_title", "event_date", "event_time", "event_location", "event_desc",  "thumbnail", "event_videos", "images", "uploaded_images"]
        # fields = ["id", "school", "event_name", "event_title", "event_date", "event_time", 
        #         "event_location", "event_desc",  "thumbnail", "event_videos", "images", "uploaded_images"]

        fields = ["id", "school", "event_name", "event_title", "event_date", "event_time", 
                "event_location", "event_desc",  "thumbnail", "event_videos", "images", "uploaded_images"]

    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        event = Events.objects.create(**validated_data)
        for image in uploaded_images:
            EventImages.objects.create(event=event, image=image)
        return event

############################################################################################################

############################################################################################################

class EventSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Events
        exclude = ['event_name']


############################################ EVENT SPEAKER ##################################################

############################################ EVENT SPEAKER ##################################################

class EventSpeakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSpeaker
        fields = ['speaker_name', 'speaker_desc']

############################################################################################################
############################################################################################################

class EventDetailSerializer(serializers.ModelSerializer):
    event_speakers = EventSpeakerSerializer(many=True)

    class Meta:
        model = Events
        # fields = ['id', 'event_name', 'event_title', 'event_date', 'event_time', 'event_location', 'event_desc', 'event_image', 'event_videos', 'event_speakers']

        fields = ['id', 'event_name', 'event_title', 'event_date', 'event_time', 
                'event_location', 'event_desc', 'event_image', 'event_videos', 'event_speakers']

#############################################################################################################


class EventSpeakersCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventSpeaker
        fields = '__all__'

