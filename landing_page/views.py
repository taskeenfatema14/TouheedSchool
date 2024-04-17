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
    allowed_methods =  [GET, GETALL] 
    related_models = {}
    
class LandingPageSchools(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = LandingPageSchoolSerializer

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
        limit = request.GET.get("limit") or 5

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
    

class SchoolEventsAPI(BaseAPIView):
    serializer_class = EventDetailSerializer
    model = Event
    allowed_methods =  [GET, GETALL, POST, PUT, DELETE] 
    related_models = {}
    
    def get(self, request,id,):
        events = Event.objects.filter(school=id)
        serialized = EventDetailSerializer(events,many=True).data
        return Response({'data':serialized},status=200) 
    
class AboutUsLP(APIView):
    def get(self, request):
        about_us = AboutUs.objects.all()
        serializer = LPAboutUs(about_us, many = True).data
        return Response({'data':serializer},status=200)
    
class GalleryView(APIView):
    def get(self, request):
        gallery = Gallery.objects.all()
        serializer = GallerySerializer(gallery, many = True).data
        return Response({'data':serializer},status=200)




# class LandingPageDetail(APIView):
#     def get_paginated_data(self, request):
#         pg = request.GET.get("pg") or 0
#         limit = request.GET.get("limit") or 20

#         # queryset = Event.objects.all()
#         events = Event.objects.all()
#         galleries = Gallery.objects.all()
#         schools = School.objects.all()
#         # Create combined data dictionary
#         combined_data = {
#             'events': events,
#             'galleries': galleries,
#             'schools': schools
#         }
        
#         count = sum([len(data) for data in combined_data.values()])
#         event_objs = combined_data['events'][
#         int(pg) * int(limit): (int(pg) + 1) * int(limit)
#         ]
#         print("Event Objects:", event_objs)
#         serializer = LPDetailSerializer(event_objs, many=True)


#         return Response({
#             "error" : False,
#             "count":count,
#             "rows" : serializer.data,
#         }, status=status.HTTP_200_OK)
    
#     def get(self, request):
#         return self.get_paginated_data(request)