
from django.shortcuts import render
from rest_framework import status
from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.pagination import PageNumberPagination
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


############################################ EVENT LIST ########################################################

from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from portals.models import *


# Create your views here.

###################################### EVENT SPEAKER PAGINATION #############################################

class EventPagination(PageNumberPagination):
    page_size = 4

############################################ EVENT LIST (NON PRIMARY KEY)########################################################

    
class EventPagination(BaseAPIView):
    page_size = 4

############################################ EVENT LIST (NON PRIMARY KEY)########################################################

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


############################################ EVENT DETAIL (USING PRIMARY KEY) ########################################################

class EventDetail(APIView): 


    def get_object(self, pk):
        try:
            return Events.objects.get(pk=pk)
        except Events.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        event = self.get_object(pk)
        serializer = EventDetailSerializer(event)
        return Response(serializer.data)
    
# class EventSpeakersPagination(PageNumberPagination):
#     page_size = 4

#     serializer = EventSerializer(event)
#     return Response(serializer.data)
    
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
    
###################################### EVENT SPEAKER PAGINATION #############################################

class EventSpeakersPagination(PageNumberPagination):
    page_size = 4

############################################ EVENT SPEAKER ##################################################


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


################################################################################################################################
        

        
###########################################################################################################

###########################################################################################################


