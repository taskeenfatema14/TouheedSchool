from rest_framework.serializers import ModelSerializer, ValidationError
from .models import *
from rest_framework import serializers

class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'