from rest_framework.serializers import ModelSerializer, ValidationError
from .models import *
from rest_framework import serializers
from events.models import *
<<<<<<< HEAD
=======

################################################# School #################################################
>>>>>>> 749970f3ea87b628f1a409a0234452924fd0221f

######################################   MY CODE    #####################################################

class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        exclude = ['created_on','updated_on']

<<<<<<< HEAD
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

class InfrastructureSerializer(ModelSerializer):
    class Meta:
        model = Infrastructure
        fields = '__all__'







=======
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
>>>>>>> 749970f3ea87b628f1a409a0234452924fd0221f
