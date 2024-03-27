from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction

# Create your views here.

class EventPagination(PageNumberPagination):
    page_size = 4

class EventView(APIView):
    pagination_class = EventPagination
    
    def get(self, request):
        paginator = self.pagination_class()
        queryset = Events.objects.all()
        paginated_queryset = paginator.paginate_queryset(queryset, request)
        serializer = EventSerializer1(paginated_queryset, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def post(self, request):
    #     event_serializer = EventSerializer(data=request.data.get('event'))
    #     speaker_serializers = [EventSpeakersCardSerializer(data=speaker_data) for speaker_data in request.data.get('speakers', [])]

    #     if event_serializer.is_valid() and all(speaker_serializer.is_valid() for speaker_serializer in speaker_serializers):
    #         with transaction.atomic():
    #             event_instance = event_serializer.save()
    #             for speaker_serializer in speaker_serializers:
    #                 speaker_serializer.save(event=event_instance)
                    
    #         return Response({
    #             "event": event_serializer.data,
    #             "speakers": [speaker_serializer.data for speaker_serializer in speaker_serializers]
    #         }, status=status.HTTP_201_CREATED)
    #     else:
    #         errors = {}
    #         if not event_serializer.is_valid():
    #             errors.update(event_serializer.errors)
    #         for i, speaker_serializer in enumerate(speaker_serializers):
    #             if not speaker_serializer.is_valid():
    #                 errors[f'speaker_{i}'] = speaker_serializer.errors
    #         return Response(errors, status=status.HTTP_400_BAD_REQUEST)

class EventDetail(APIView): 

    def get(self, request, pk):
        try:
            events = Events.objects.get(pk=pk)
        except Events.DoesNotExist:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EventSerializer1(events)
        return Response(serializer.data)
    
    def put(self, request, pk):
        event = self.get_object(pk)
        serializer = EventSerializer(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EventSpeakersPagination(PageNumberPagination):
    page_size = 4

class EventSpeakersCard(APIView):
    
    pagination_class = EventSpeakersPagination  
    def post(self, request):
        serializer = EventSpeakersCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get(self, request, format=None):
        paginator = EventSpeakersPagination()
        event_speakers = EventSpeaker.objects.all()
        result_page = paginator.paginate_queryset(event_speakers, request)
        serializer = EventSpeakersCardSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
class EventSpeakersCardPK(APIView):

    # def get(self, request, pk):
    #     try:
    #         events = Events.objects.get(pk=pk)
    #     except Events.DoesNotExist:
    #         return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

    #     serializer = EventSpeakersCardPK(events)
    #     return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        event_speaker = self.get_object(pk)
        serializer = EventSpeakersCardSerializer(event_speaker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        event_speaker = self.get_object(pk)
        event_speaker.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)