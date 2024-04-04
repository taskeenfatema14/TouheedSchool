from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
from events.models import *


class LandingPgSchoolSerailizer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['image', 'location', 'name', 'description'] 
class LandingPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['event_title','event_image']

class LandinPageSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fiels = ['name', 'image', 'location']