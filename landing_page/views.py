from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.views import APIView
from events.models import *
from rest_framework.response import Response
from rest_framework import status
from portals.base import BaseAPIView
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse
from rest_framework import generics

# Create your views here.

class LandingPageApi(APIView):
    
    def get(self, request):
        page = Event.objects.all()
        serializer = LandingPageSerializer(page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LandingPageSchool(BaseAPIView):

    serializer_class = LandingPgSchoolSerailizer
    model = School
    allowed_methods =  [GET, GETALL, POST, PUT, DELETE] 
    related_models = {}
    
class LandingPageSchools(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = LandinPageSchoolSerializer

class LPLatestEvents(APIView):
    def get(self, request):
        events = Event.objects.all().order_by('-created_on')
        serializer = LPLatestEventsSerializer(events, many = True)
        return Response(serializer.data)
        