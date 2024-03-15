from rest_framework.serializers import ModelSerializer
from .models import User
from rest_framework import serializers
from schools.models import School

class UserSerializer(ModelSerializer):
    school_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        exclude = ['last_login', 'date_joined', 'school']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()
        
        return user
    
    def get_school_name(self, obj):
        if obj.school:
            return obj.school.name
        return None