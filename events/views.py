from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from portals.base import BaseAPIView
from portals.constants import *

# Create your views here.

class EventAPIView(APIView):

    def get(self, request, id):  
        events = Event.objects.filter(school=id).order_by('-created_on')
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class EventView(BaseAPIView):
    serializer_class = EventSerializer1
    model = Event
    allowed_methods =  [GETALL] 
    related_models = {}

from math import ceil
class EventDetails(APIView):
    def get_paginated_data(self, request):
        pg = request.GET.get("pg") or 0
        limit = request.GET.get("limit") or 20

        queryset = Event.objects.all().prefetch_related('images', 'speakers')
        count = queryset.count()
        pages_count = ceil(count / int(limit))  # Calculate total number of pages
        objs = queryset[
            int(pg) * int(limit) : (int(pg)+1)*int(limit)
        ]
        serializer = EventDetailSerializer(objs, many = True)

        return Response({
            "error" : False,
            "pages_count": pages_count,
            "count":count,
            "rows" : serializer.data,
        }, status=status.HTTP_200_OK)
    
    def get(self, request):
        return self.get_paginated_data(request)

class EventSpeakersCard(BaseAPIView):
    serializer_class = EventSpeakersCardSerializer
    model = EventSpeaker
    allowed_methods =  [GET, GETALL, POST, PUT, DELETE] 
    related_models = {}

class SingleEventDetail(APIView):
    def get(self, request, id):
        try:
            event = Event.objects.get(id=id)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # def get(self, request, id):
    #     try:
    #         school = get_object_or_404(School, id=id)
    #         event = Event.objects.filter(school=school).first()
    #         if event:
    #             serializer = SingleEventSerializer(event)
    #             return Response(serializer.data)
    #         else:
    #             return Response({"detail": "No event found for this school"}, status=status.HTTP_404_NOT_FOUND)
    #     except School.DoesNotExist:
    #         return Response({"detail": "School not found"}, status=status.HTTP_404_NOT_FOUND)