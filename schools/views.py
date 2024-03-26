from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from rest_framework.response import Response
from rest_framework import status
from portals.base import BaseAPIView

from portals.constants import (
    GETALL,
    GET,
    POST,
    PUT
)
# Create your views here.

class SchoolApi(APIView):
    def post(self, request):
        serializer = SchoolSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        camp = School.objects.all()
        serializer = SchoolSerializer(camp,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class SchoolPutDeleteApi(APIView):
    def put(self, request,id):
        try:
            instance = School.objects.get(pk=id)
        except School.DoesNotExist:
            return Response({"error" : "School not found"}, status=status.HTTP_404_NOT_FOUND)
        serializer = SchoolSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try:
            instance = School.objects.get(pk=id)
            instance.delete()
            return Response({"message" : "School deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except School.DoesNotExist:
            return Response({"error": "School not found"}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

class SchoolApiPagination(APIView):
    def get(self, request):
        params = request.GET
        page_number = int(params.get("pg", 1))
        page_size = int(params.get("limit", 3 ))
        offset = (page_number - 1) * page_size
        limit = page_size

        schools = School.objects.all()[offset:offset + limit]
        serializer = SchoolSerializer(schools, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

#*******************************************  SCHOOL TRIAL  *******************************************#

class SchoolgetAPI(BaseAPIView):
    serializer_class = SchoolSerializer
    model = School
    allowed_methods = [GET, GETALL]
    related_models = {}




#*******************************************  CONTACT US  *******************************************#

class ContactUsApi(APIView):
    def post(self, request):
        serializer = ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Contact Send Successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        
    def get(self, request):
        school = request.data.get('school')
        if school:
            contacts = ContactUs.objects.filter(school=school)
            serializer = ContactUsSerializer(contacts, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Please provide a school_id parameter"}, status=status.HTTP_400_BAD_REQUEST)
    
class ContactUsAll(APIView):
    def get(self, request):
        contact = ContactUs.objects.all()
        serializer = ContactUsSerializer(contact, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    



#*******************************************  LANDING PAGE  *******************************************#

class LandingPageApi(APIView):
    def get(self, request):
        page = Events.objects.all()
        serializer = LandingPageSerializer(page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



#*******************************************  INFRASTRUCTURE  *******************************************#

class InfrastructureAPI(BaseAPIView):
    serializer_class = InfrastructureSerializer
    model = Infrastructure
    allowed_methods =  [GET, GETALL, POST, PUT] 
    related_models = {}

    def post(self, request, *args, **kwargs):
        serializer = InfrastructureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)
    
    def put(self, request,id=None, *args, **kwargs):
        return super().put(request, id, *args, **kwargs)


