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
        fields = ['id','event_title','event_image']

class LandingPageSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = ['id','name', 'image', 'location']

class SchoolSerializer(serializers.ModelSerializer):
    class Meta: 
        model = School
        fields = ['name']

class LPLatestEventsSerializer(serializers.ModelSerializer):
    school = SchoolSerializer()

    class Meta:
        model = Event
        fields = ['id','title','desc', 'thumbnail', 'school','name']


class LPInfrastructureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Infrastructure
        fields = ['id','image', 'title']

class LPReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','username', 'description'] 

class LPAboutUs(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = ['id', 'desc', 'videos']

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gallery
        fields = ['id', 'image']



# class LPDetailSerializer(serializers.ModelSerializer):
#     landing_pg = LandingPageSerializer(many = True,read_only=True)
#     about_us = LPAboutUs(many = True,read_only=True)
#     our_schools = LandingPageSchoolSerializer(many = True,read_only=True)
#     latest_events = LPLatestEventsSerializer(many = True,read_only=True)
#     our_best_features = LPInfrastructureSerializer(many = True,read_only=True)
#     testimonials = LPReviewSerializer(many = True,read_only=True)
#     gallery = GallerySerializer(many = True,read_only=True)

#     class Meta:
#         model = Event
#         fields = ['id','title','desc', 'thumbnail', 'landing_pg', 'about_us', 'our_schools', 
#                   'latest_events', 'our_best_features', 'testimonials', 'gallery']