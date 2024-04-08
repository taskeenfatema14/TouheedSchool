from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
from events.models import *
from events.serializers import *
from reviews.models import *

class LandingPgSchoolSerailizer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id','image', 'location', 'name', 'description']

class LandingPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['event_title','event_image']

class LandinPageSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fiels = ['name', 'image', 'location']

class LPLatestEventsSerializer(serializers.ModelSerializer):
    # images = EventImageSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = ["title", "desc", 'thumbnail']
        # fields = ['images', "title", "desc", 'thumbnail']

    # def to_representation(self, instance):
    #     data = super().to_representation(instance)
    #     if 'images' not in data:
    #         images = instance.eventimages_set.all()  
    #         data['images'] = EventImageSerializer(images, many=True).data
    #     return data


class LPInfrastructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infrastructure
        fields = ['image', 'title']

class LPReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['username', 'description'] #Profile picture incomplete