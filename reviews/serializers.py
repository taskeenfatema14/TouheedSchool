from rest_framework.serializers import ModelSerializer
from .models import *
from rest_framework import serializers

class BoardMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardMember
        fields = ['board_id', 'school', 'name','title','description','image'] 

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['review_id', 'school', 'username','time','date','rating'] 

class MailLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MailLog
        fields = '__all__'