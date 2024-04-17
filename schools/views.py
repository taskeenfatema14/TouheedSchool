from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.views import APIView
from events.models import *
from rest_framework import generics
from rest_framework.views import APIView
from .serializers import *
from .models import *
from django.conf import settings
from django.http import Http404

from rest_framework.response import Response
from rest_framework import status
from portals.base import BaseAPIView
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse
from .email import EmailService


class SchoolApi(BaseAPIView):
    serializer_class = SchoolSerializer
    model = School
    allowed_methods =  [GET, GETALL, POST, PUT, DELETE] 
    related_models = {}
        

class ContactUsApi(APIView):
    def post(self, request, *args, **kwargs):
        # Assuming you have a serializer for ContactUs model
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            contact_us_instance=serializer.save()

            # Sending confirmation email to the user
            user_subject = 'Contact Us'
            user_message = 'Thank you for contacting us. We will get back to you soon.'
            user_email_service = EmailService(user_subject, user_message, [serializer.data['user_email']])
            user_email_service.send()

            # Sending email to the school
            school_email = contact_us_instance.school.school_email
            school_subject = 'New Contact Inquiry'
            school_message = f'A new contact inquiry has been received from {serializer.data["full_name"]}.'
            school_email_service = EmailService(school_subject, school_message, [school_email])
            print(school_email_service)
            school_email_service.send()
            print('sending emails done!')

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InfrastructureAPI(BaseAPIView):
    serializer_class = InfrastructureSerializer
    model = Infrastructure
    allowed_methods =  [GET, GETALL, POST, PUT, DELETE] 
    related_models = {}

    def put(self, request,id=None, *args, **kwargs):
        if id is None:
            return Response({"error":"ID is required"}, status=400)
        try:
            obj= Infrastructure.objects.get(id=id)
        except Infrastructure.DoesNotExist:
            return Response({"error":"Object does not exist"}, status=400)
        serializer = InfrastructurePutSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)

class FaqApi(BaseAPIView):
    serializer_class = FaqSerializer
    model = FrequentlyAskedQuestion
    allowed_methods =  [GET, GETALL, POST, PUT, DELETE] 
    related_models = {}


class NoticeboardApi(BaseAPIView):
    serializer_class = NoticeBoardSerializer
    model = Noticeboard
    allowed_methods =  [GET, GETALL, POST, PUT, DELETE] 
    related_models = {}


class SchoolEventApi(APIView):
    # serializer_class = SchoolEventSerializer
    # model = Event
    # allowed_methods = [GET, GETALL]
    # related_models = {}

    def get(self, request, format=None):
        events = Event.objects.prefetch_related('images').all()  # Assuming 'eventimages_set' is the related name
        serializer = SchoolEventSerializer(events, many=True)
        return Response(serializer.data)
    
class SchoolDetailAPiView(APIView):
    def get_paginated_data(self, request):
        pg = request.GET.get("pg") or 0
        limit = request.GET.get("limit") or 20

        queryset = School.objects.all().prefetch_related('frequentlyquestion_set', 'infrastructure','notice_board_set')
        count = queryset.count()
        objs = queryset[
            int(pg) * int(limit) : (int(pg)+1)*int(limit)
        ]   
        serializer = SchoolDetailSerializer(objs, many = True)

        return Response({
            "error" : False,
            "count":count,
            "rows" : serializer.data,
        }, status=status.HTTP_200_OK)
    
    def get_by_id(self, request, id):
        try:
            school = School.objects.get(id=id)
            serializer = SchoolDetailSerializer(school)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except School.DoesNotExist:
            return Response({"error": True, "message": "School not found"}, status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id=None):
        if id is not None:
            return self.get_by_id(request, id)
        else:
            return self.get_paginated_data(request)
        

class AboutUs(APIView): 
    def get_object(self, pk):
        try:
            return School.objects.get(pk=pk)
        except School.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        user = self.get_object(pk)
        serializer = AboutUsSerializer(user)
        return Response(serializer.data)
