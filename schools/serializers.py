from rest_framework.serializers import ModelSerializer, ValidationError
from .models import *
from rest_framework import serializers

class BoardMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardMember
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'

class MailLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailLog
        fields = '__all__'