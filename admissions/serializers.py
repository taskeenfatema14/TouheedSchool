from rest_framework import serializers
from .models import *

# class RegisterFormSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = RegisterForm
#         fields = '__all__'

class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        exclude = ('created_on','updated_on','is_deleted')