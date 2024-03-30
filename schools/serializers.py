from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers
from events.models import *


class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = ['id','name','location', 'image','video','facility','decription','contact_no','school_email','principal']


class LandingPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Events
        fields = ['event_title','event_image']

class LandinPageSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fiels = ['name', 'image', 'location']
        exclude = ['created_on','updated_on']
        

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

class InfrastructureSerializer(ModelSerializer):
    class Meta:
        model = Infrastructure
        fields = '__all__'

class FaqSerializer(ModelSerializer):
    class Meta:
        model = FrequentlyAskedQuestions
        fields = '__all__'

