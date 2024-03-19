from django.shortcuts import render
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, permissions

# Create your views here.

############################################ SCHOOLS ########################################################

class SchoolApi(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    
class SchoolPutDeleteApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

############################################ EVENT LIST ########################################################
    
class EventPagination(PageNumberPagination):
    page_size = 4

class EventView(APIView):
    pagination_class = EventPagination
    
    def get(self, request):
        events = Events.objects.all()
        paginator = self.pagination_class()
        paginated_events = paginator.paginate_queryset(events, request)
        serializer = EventSerializer1(paginated_events, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Events.objects.all()
    serializer_class = EventSerializer
    
############################################ EVENT DETAILS API ########################################################

class EventFullDetail(APIView):
    def get_object(self, pk):
        try:
            return Events.objects.get(pk=pk)
        except Events.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        event = self.get_object(pk)
        serializer = EventDetailSerializer(event)
        return Response(serializer.data)
    
class EventSpeakersPagination(PageNumberPagination):
    page_size = 4

class EventSpeakersCard(APIView):
    
    pagination_class = EventSpeakersPagination
    
    def get_object(self, pk):
        try:
            return Events.objects.get(pk=pk)
        except Events.DoesNotExist:
            raise Http404
        
    def get(self, request, pk):
        event = self.get_object(pk)
        speakers = event.event_speakers.all().order_by('id') 
        
        paginator = self.pagination_class()
        result_page = paginator.paginate_queryset(speakers, request)
        
        serializer = EventSpeakersCardSerializer(result_page, many=True) 
        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request):
        serializer = EventSpeakersCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


