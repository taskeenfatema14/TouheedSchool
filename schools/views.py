from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.views import APIView
from events.models import *
from django.conf import settings
from django.http import Http404
from django.core.mail import send_mail
from core.settings import EMAIL_HOST_USER
from rest_framework.response import Response
from rest_framework import status
from portals.base import BaseAPIView
from django.core.paginator import Paginator, EmptyPage
from django.urls import reverse



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
        

# class SchoolApiPagination(APIView):
#     def get(self, request):
#         params = request.GET
#         page_number = int(params.get("pg", 1))
#         page_size = int(params.get("limit", 3 ))
#         page_size = int(params.get("limit", 6 ))
#         offset = (page_number - 1) * page_size
#         limit = page_size

#         schools = School.objects.all()[offset:offset + limit]
#         serializer = SchoolSerializer(schools, many=True)

#         return Response(serializer.data, status=status.HTTP_200_OK)
        

class SchoolApiPagination(APIView):

    serializer_class = SchoolSerializer
    model = School

    def get_paginated_data(self, request):
        limit = max(int(request.GET.get('limit', 0)), 5) 
        page_number = max(int(request.GET.get('page', 0)), 1)
        
        queryset = self.model.objects.all()
        paginator = Paginator(queryset, limit)
        
        try:
            paginated_queryset = paginator.page(page_number)
        except EmptyPage:
            return Response({"error": True, "message": "Page not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(paginated_queryset, many=True)
        
        return Response({
            "error": False,
            "pages_count": paginator.num_pages,
            "count": paginator.count,
            "rows": serializer.data
        }, status=status.HTTP_200_OK)

    def get(self, request):
        return self.get_paginated_data(request)


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



#*******************************************  INFRASTRUCTURE  *******************************************#

class InfrastructureAPI(APIView):
    # serializer_class = InfrastructureSerializer
    # model = Infrastructure
    # allowed_methods =  [GET, GETALL, POST, PUT] 
    # related_models = {}

    # def post(self, request, *args, **kwargs):
    #     serializer = InfrastructureSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=200)
    #     return Response(serializer.errors, status=400)
    
    # def put(self, request,id=None, *args, **kwargs):
    #     return super().put(request, id, *args, **kwargs)


    def post(self, request):
        serializer = InfrastructureSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request):
        camp = Infrastructure.objects.all()
        serializer = InfrastructureSerializer(camp,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class InfrastructurePaginationApi(APIView):
    serializer_class = InfrastructureSerializer
    model = Infrastructure

    def get_paginated_data(self, request):
        limit = max(int(request.GET.get('limit', 0)), 5) 
        page_number = max(int(request.GET.get('page', 0)), 1)
        
        queryset = self.model.objects.all()
        paginator = Paginator(queryset, limit)
        
        try:
            paginated_queryset = paginator.page(page_number)
        except EmptyPage:
            return Response({"error": True, "message": "Page not found"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = self.serializer_class(paginated_queryset, many=True)
        
        return Response({
            "error": False,
            "pages_count": paginator.num_pages,
            "count": paginator.count,
            "rows": serializer.data
        }, status=status.HTTP_200_OK)

    def get(self, request):
        return self.get_paginated_data(request)

class FaqApi(BaseAPIView):
    serializer_class = FaqSerializer
    model = FrequentlyAskedQuestions
    allowed_methods =  [GET, GETALL, POST, PUT, DELETE] 
    related_models = {}

    def get(self, request):
        camp = FrequentlyAskedQuestions.objects.all()
        serializer = FaqSerializer(camp,many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def post(self, request):
    #     serializer = FaqSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # def get(self, request):
    #     camp = FrequentlyAskedQuestions.objects.all()
    #     serializer = FaqSerializer(camp,many = True)
    #     return Response(serializer.data, status=status.HTTP_200_OK)