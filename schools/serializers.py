from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
from events.models import *


class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        exclude = ['created_on','updated_on']      

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

class InfrastructureSerializer(ModelSerializer):
    class Meta:
        model  = Infrastructure
        fields = '__all__'

class InfrastructurePutSerializer(ModelSerializer):
    class Meta:
        model = Infrastructure
        fields = '__all__'
        extra_kwargs = {
            'title': {'required': False},
            'school': {'required': False}
        }

class FaqSerializer(ModelSerializer):
    class Meta:
        model  = FrequentlyAskedQuestion
        fields = '__all__'

class NoticeBoardSerializer(ModelSerializer):
    class Meta:
        model  = Noticeboard
        fields = '__all__'


class EventImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImages
        fields = ['image']

class SchoolEventSerializer(serializers.ModelSerializer):
    images = EventImagesSerializer(many=True, read_only=True)

    class Meta: 
        model = Event
        fields = ['title', 'date', 'time', 'location', 'desc', 'images']