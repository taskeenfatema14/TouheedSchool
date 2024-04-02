from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction
from portals.base import BaseAPIView
from portals.constants import *

# Create your views here.

class EventView(BaseAPIView):
    serializer_class = EventSerializer
    model = Event
    allowed_methods =  [GET, GETALL, POST, PUT, DELETE] 
    related_models = {}

class EventSpeakersCard(BaseAPIView):
    
    serializer_class = EventSpeakersCardSerializer
    model = EventSpeaker
    allowed_methods =  [GET, GETALL, POST, PUT, DELETE] 
    related_models = {}

class EventCreateAPIView(APIView):
    def post(self, request):
        event_data = request.data.get('event')
        image_data = request.data.get('images')
        speaker_data = request.data.get('speakers')
        
        with transaction.atomic():
            event = EventSerializer(data=event_data)
            if event.is_valid():
                events = event.save()
            else:
                return Response(event.errors, status=status.HTTP_400_BAD_REQUEST)
            
            image_serializer = EventImageSerializer(data=image_data, many=True)
            if image_serializer.is_valid():
                for image in image_data:
                    EventImages.objects.create(event=events, **image)
            else:
                return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
            speaker_serializer = EventSpeakersCardSerializer(data=speaker_data, many=True)
            if speaker_serializer.is_valid():
                for speaker in speaker_data:
                    EventSpeaker.objects.create(event=events, **speaker)
            else:
                return Response(speaker_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                
        return Response("Event created successfully", status=status.HTTP_201_CREATED)
