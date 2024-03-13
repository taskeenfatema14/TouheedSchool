<<<<<<< HEAD
from rest_framework import serializers
from .models import *

class BoardMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardMember
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
=======
from rest_framework.serializers import ModelSerializer, ValidationError
from .models import *
from rest_framework import serializers

class SchoolSerializer(ModelSerializer):
    class Meta:
        model = School
        fields = '__all__'
>>>>>>> 162d812960618f74654658bb586d0e08fda77e96
