from django.db import models
from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers

from rest_framework_simplejwt.tokens import RefreshToken

# Model
from django.contrib.auth.models import User
from .models import *
from django.conf import settings
from django.template.defaultfilters import truncatechars




class EventImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventImages
        fields = "__all__"

class EventSerializer(serializers.ModelSerializer):
    date = serializers.SerializerMethodField(read_only = True)
    date_abbreviated = serializers.SerializerMethodField(read_only = True)
    time = serializers.SerializerMethodField(read_only = True)
    short_description = serializers.SerializerMethodField(read_only = True)
    all_images = serializers.SerializerMethodField(read_only = True)

    class Meta:
        model = Event
        fields = "__all__"

    def get_short_description(self, obj):
        return truncatechars(obj.event_desc, 100)

    def get_all_images(self,obj):
        all_image = obj.eventimages_set.all()
        serializers = EventImagesSerializer(all_image, many=True)
        return serializers.data

    def get_date(self, obj):
        return  obj.event_date.strftime(format=settings.DATE_FORMAT) if obj.event_date else "-"

    def get_date_abbreviated(self, obj):
        return obj.event_date.strftime(format="%d %b") if obj.event_date else "-"


    def get_time(self,obj):
        return  obj.event_date.strftime(format=settings.TIME_FORMAT) if obj.event_date else "-"
             




class UserSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField(read_only=True)
    id = serializers.SerializerMethodField(read_only=True)
    isAdmin = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name', 'isAdmin']

    def get_id(self, obj):
        return obj.id

    def get_isAdmin(self, obj):
        return obj.is_staff

    def get_name(self, obj):
        name = obj.first_name
        if name == '':
            name = obj.email

        return name

class UserSerializerWithToken(UserSerializer):
    token = serializers.SerializerMethodField(read_only = True)
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'name','isAdmin', 'token']

    def get_token(self, obj):
        token = RefreshToken.for_user(obj)
        return str(token.access_token)


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"