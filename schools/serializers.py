from rest_framework.serializers import ModelSerializer, ValidationError
from .models import *
from rest_framework import serializers


######## KOMAL ########

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = '__all__'

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



######################################   MY CODE    #####################################################



class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class ContactUsSerializer(ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

# class LandingPageSerializer(ModelSerializer):
#     class Meta:
#         model = Events
#         fields = ['event_title','event_image','']


class SchoolSerializer1(ModelSerializer):
    class Meta:
        model = School
        fields = ['name']  

class LandingPageSerializer(ModelSerializer):
    school = SchoolSerializer1()

    class Meta:
        model = Events
        fields = ['event_title', 'event_image', 'school']  

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['school_name'] = data['school']['name']
        del data['school']  





