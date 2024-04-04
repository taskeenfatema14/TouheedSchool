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
from schools.models import *
from reviews.models import *

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

class LatestEvents(APIView):

    def get_paginated_data(self, request):
        pg = request.GET.get("pg") or 0
        limit = request.GET.get("limit") or 20

        queryset = Event.objects.order_by('-created_on')
        count = queryset.count()
        objs = queryset[
            int(pg) * int(limit) : (int(pg)+1)*int(limit)
        ]
        serializer = LPLatestEventsSerializer(objs, many = True)

        return Response({
            "error" : False,
            "count":count,
            "rows" : serializer.data,
        }, status=status.HTTP_200_OK)
    
    def get(self, request):
        return self.get_paginated_data(request)
    
class InfrastructureAPI(APIView):  

    def get_paginated_data(self, request):
        pg = request.GET.get("pg") or 0
        limit = request.GET.get("limit") or 20

        queryset = Infrastructure.objects.order_by('-created_on')
        count = queryset.count()
        objs = queryset[
            int(pg) * int(limit) : (int(pg)+1)*int(limit)
        ]
        serializer = LPInfrastructureSerializer(objs, many = True)

        return Response({
            "error" : False,
            "count":count,
            "rows" : serializer.data,
        }, status=status.HTTP_200_OK)
    
    def get(self, request):
        return self.get_paginated_data(request)
    
class Testimonials(APIView):

    def get_paginated_data(self, request):
        pg = request.GET.get("pg") or 0
        limit = request.GET.get("limit") or 20

        queryset = Review.objects.order_by('-created_on')
        count = queryset.count()
        objs = queryset[
            int(pg) * int(limit) : (int(pg)+1)*int(limit)
        ]
        serializer = LPReviewSerializer(objs, many = True)

        return Response({
            "error" : False,
            "count":count,
            "rows" : serializer.data,
        }, status=status.HTTP_200_OK)
    
    def get(self, request):
        return self.get_paginated_data(request)