from rest_framework import status
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db import transaction
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse

# Create your views here.

class EventView(APIView):

    def get_paginated_data(self, request):
        limit = max(int(request.GET.get('limit', 0)), 4)  
        page_number = max(int(request.GET.get('page', 0)), 1)
        
        queryset = Events.objects.all()
        
        paginator = Paginator(queryset, limit)
        
        try:
            paginated_queryset = paginator.page(page_number)
        except EmptyPage:
            return Response({"error": True, "message": "Page not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EventSerializer(paginated_queryset, many=True)
        
        next_page_url = None
        if paginated_queryset.has_next():
            next_page_number = paginated_queryset.next_page_number()
            next_page_url = reverse('events-np') + f'?page={next_page_number}&limit={limit}'

        return Response({
            "error": False,
            "pages_count": paginator.num_pages,
            "count": paginator.count,
            "rows": serializer.data,
            "next_page_url": next_page_url
        }, status=status.HTTP_200_OK)

    def get(self, request):
        return self.get_paginated_data(request)
    
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class EventDetail(APIView): 

    def get(self, request, pk):
        try:
            events = Events.objects.get(pk=pk)
        except Events.DoesNotExist:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EventSerializer1(events)
        return Response(serializer.data)
    
    def put(self, request, pk):
        try:
            event = Events.objects.get(pk=pk)
        except Events.DoesNotExist:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EventSerializer1(event, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            event = Events.objects.get(pk=pk)
        except Events.DoesNotExist:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

        event.delete()
        return Response({"error": "Successfully deleted event"},status=status.HTTP_204_NO_CONTENT)

class EventSpeakersCard(APIView):
    
    def post(self, request):
        serializer = EventSpeakersCardSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def get_paginated_data(self, request):
        limit = max(int(request.GET.get('limit', 0)), 4)  
        page_number = max(int(request.GET.get('page', 0)), 1)
        
        queryset = EventSpeaker.objects.all()
        
        paginator = Paginator(queryset, limit)
        
        try:
            paginated_queryset = paginator.page(page_number)
        except EmptyPage:
            return Response({"error": True, "message": "Page not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = EventSpeakersCardSerializer(paginated_queryset, many=True)
        
        next_page_url = None
        if paginated_queryset.has_next():
            next_page_number = paginated_queryset.next_page_number()
            next_page_url = reverse('speaker-card') + f'?page={next_page_number}&limit={limit}'

        return Response({
            "error": False,
            "pages_count": paginator.num_pages,
            "count": paginator.count,
            "rows": serializer.data,
            "next_page_url": next_page_url
        }, status=status.HTTP_200_OK)

    def get(self, request):
        return self.get_paginated_data(request)
    
class EventSpeakersCardPK(APIView):

    def get(self, request, pk):
        try:
            events = EventSpeaker.objects.get(pk=pk)
        except EventSpeaker.DoesNotExist:
            return Response({"error": "Event not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EventSpeakersCardSerializer(events)
        return Response(serializer.data)
    
    def put(self, request, pk, format=None):
        try:
            event_speaker = EventSpeaker.objects.get(pk=pk)
        except EventSpeaker.DoesNotExist:
            return Response({"error": "Event speaker not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = EventSpeakersCardSerializer(event_speaker, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        try:
            event_speaker = EventSpeaker.objects.get(pk=pk)
        except EventSpeaker.DoesNotExist:
            return Response({"error": "Event speaker not found"}, status=status.HTTP_404_NOT_FOUND)

        event_speaker.delete()
        return Response({"error": "Successfully deleted Event speaker"}, status=status.HTTP_204_NO_CONTENT)
    