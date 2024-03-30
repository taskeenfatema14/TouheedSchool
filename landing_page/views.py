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
        page = Events.objects.all()
        serializer = LandingPageSerializer(page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class LandingPageSchool(APIView):

    def get_paginated_data(self, request):
        limit = max(int(request.GET.get('limit', 0)), 5)
        page_number = max(int(request.GET.get('page', 0)), 1)
        
        queryset = School.objects.all()
        
        paginator = Paginator(queryset, limit)
        
        try:
            paginated_queryset = paginator.page(page_number)
        except EmptyPage:
            return Response({"error": True, "message": "Page not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = LandingPgSchoolSerailizer(paginated_queryset, many=True)
        
        next_page_url = None
        if paginated_queryset.has_next():
            next_page_number = paginated_queryset.next_page_number()
            next_page_url = reverse('landing-pg-school') + f'?page={next_page_number}&limit={limit}'

        return Response({
            "error": False,
            "pages_count": paginator.num_pages,
            "count": paginator.count,
            "rows": serializer.data,
            "next_page_url": next_page_url
        }, status=status.HTTP_200_OK)

    def get(self, request):
        return self.get_paginated_data(request)
    
class LandingPageSchools(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = LandinPageSchoolSerializer
        