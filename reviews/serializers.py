from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers

class BoardMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardMember
        fields = "__all__"

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id','school', 'username','time','date','rating','description'] 
