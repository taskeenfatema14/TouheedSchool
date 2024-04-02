from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.views import APIView
from events.models import *
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
    # def post(self, request):
    #     serializer = ContactUsSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response({"message": "Contact Send Successfully"}, status=status.HTTP_201_CREATED)
    #     else:
    #         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
        
#     def get(self, request):
#         school = request.data.get('school')
#         if school:
#             contacts = ContactUs.objects.filter(school=school)
#             serializer = ContactUsSerializer(contacts, many=True)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({"error": "Please provide a school_id parameter"}, status=status.HTTP_400_BAD_REQUEST)
    
# class ContactUsAll(APIView):
#     def get(self, request):
#         contact = ContactUs.objects.all()
#         serializer = ContactUsSerializer(contact, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)



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


