from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
from events.models import *
from events.serializers import *

class LandingPgSchoolSerailizer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['image', 'location', 'name', 'description']

class LandingPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_title','event_image']

class LandinPageSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fiels = ['name', 'image', 'location']

class LPLatestEventsSerializer(serializers.ModelSerializer):
    images = EventImageSerializer(many = True, read_only = True)
    class Meta:
        model = Event
        fields = ['images', "title", "desc"]

class LPInfrastructure(serializers.ModelSerializer):
    class Meta:
        model = Infrastructure
        fields = ['image', 'title']