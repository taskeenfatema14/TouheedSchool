from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction
from portals.base import BaseAPIView
from portals.constants import *

# Create your views here.

class EventAPIView(BaseAPIView):

    serializer_class = EventSerializer
    model = Event
    allowed_methods =  [GET, GETALL] 
    related_models = {}
    
class EventView(BaseAPIView):
    serializer_class = EventSerializer1
    model = Event
    allowed_methods =  [GETALL] 
    related_models = {}

class EventDetails(APIView):
    def get_paginated_data(self, request):
        pg = request.GET.get("pg") or 0
        limit = request.GET.get("limit") or 20

        queryset = Event.objects.all().prefetch_related('images', 'speakers')
        count = queryset.count()
        objs = queryset[
            int(pg) * int(limit) : (int(pg)+1)*int(limit)
        ]
        serializer = EventDetailSerializer(objs, many = True)

        return Response({
            "error" : False,
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

