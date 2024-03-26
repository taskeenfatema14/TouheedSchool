from rest_framework.serializers import ModelSerializer, ValidationError
from .models import *
from rest_framework import serializers
from events.models import *

################################################# School #################################################

################################################# School #################################################

######################################   MY CODE    #####################################################

class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        exclude = ['created_on','updated_on']

##################################### LANDING PAGE ########################################################

# class LandingPageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Events
#         fields = ['event_title','event_image','']

##################################### LANDING PAGE SCHOOLS ################################################

class LandinPageSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fiels = ['name', 'image', 'location']
        
########################################## CONTACT US #######################################################

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '_all_'

############################################################################################################

##################################### LANDING PAGE ########################################################

# class LandingPageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Events
#         fields = ['event_title','event_image','']

##################################### LANDING PAGE SCHOOLS ################################################

class LandinPageSchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fiels = ['name', 'image', 'location']
        
########################################## CONTACT US #######################################################

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '_all_'

############################################################################################################
