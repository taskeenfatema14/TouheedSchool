from rest_framework.serializers import ModelSerializer, ValidationError
from .models import *
from rest_framework import serializers
from events.models import *

######################################   MY CODE    #####################################################

class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class ContactUsSerializer(ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'

# class EventLandingSerializer(ModelSerializer):
#     class  Meta:
#         models = 

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







