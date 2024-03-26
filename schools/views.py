from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.views import APIView
from events.models import *
# views.py
from rest_framework import generics
from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from .models import *
from django.conf import settings
from django.http import Http404
from django.core.mail import send_mail
from core.settings import EMAIL_HOST_USER
from rest_framework.response import Response
from rest_framework import status
from portals.base import BaseAPIView


############################################ SCHOOLS ########################################################

class SchoolApi(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    
class SchoolPutDeleteApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

############################################ LANDING PAGE ####################################################

# class LandingPageApi(APIView):
#     def get(self, request):
#         page = Events.objects.all()
#         serializer = LandingPageSerializer(page, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
########################################### LANDING PAGE 5 SCHOOLS #######################################################

class LandingPageSchools(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = LandinPageSchoolSerializer

###############################################################################################################

class BoardMemberListCreate(generics.ListCreateAPIView):
    queryset = BoardMember.objects.all()
    serializer_class = BoardMemberSerializer

class BoardMemberRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BoardMember.objects.all()
    serializer_class = BoardMemberSerializer

################################REVIEW############################################################

# class ReviewListCreateAPIView(generics.ListCreateAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

# class ReviewRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
class ReviewListCreateAPIView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReviewRetrieveUpdateDestroyAPIView(APIView):
    def get_object(self, pk):
        try:
            return Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            raise Http404
    
    def get(self, request, pk):
        review = self.get_object(pk)
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def delete(self, request, pk):
        review = self.get_object(pk)
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
###################################Maillog#############################################
class MailLogAPIView(APIView):
    def get(self, request):                                 
        try:
            mail_logs = MailLog.objects.all()
            serializer = MailLogSerializer(mail_logs, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def post(self, request):
        serializer = MailLogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            mail_log = MailLog.objects.get(pk=pk)
        except MailLog.DoesNotExist:
            return Response({"error": "Mail log does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = MailLogSerializer(mail_log, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            mail_log = MailLog.objects.get(pk=pk)
        except MailLog.DoesNotExist:
            return Response({"error": "Mail log does not exist"}, status=status.HTTP_404_NOT_FOUND)
        
        mail_log.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




######################taskeen#################################
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
        page_size = int(params.get("limit", 6 ))
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


# class LandingPageApi(APIView):
#     def get(self, request):
#         page = Events.objects.all()
#         serializer = LandingPageSerializer(page, many=True)

# class LandingPageApi(APIView):
#     def get(self, request):
#         page = Events.objects.all()
#         serializer = LandingPageSerializer(page, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.data, status=status.HTTP_200_OK)
                # return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

###############################################################
