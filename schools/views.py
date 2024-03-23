from rest_framework import generics
from .models import *
from .serializers import *
from rest_framework.views import APIView
from events.models import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

############################################ SCHOOLS ########################################################

class SchoolApi(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    
class SchoolPutDeleteApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer

############################################ LANDING PAGE ####################################################

class LandingPageApi(APIView):
    def get(self, request):
        page = Events.objects.all()
        serializer = LandingPageSerializer(page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
########################################### LANDING PAGE 5 SCHOOLS #######################################################

class LandingPageSchools(generics.ListAPIView):
    queryset = School.objects.all()
    serializer_class = LandinPageSchoolSerializer

###############################################################################################################

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
        page_size = int(params.get("limit", 6 ))
        offset = (page_number - 1) * page_size
        limit = page_size

        schools = School.objects.all()[offset:offset + limit]
        serializer = SchoolSerializer(schools, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

################################   CONTACT US    #################################

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
    

class LandingPageApi(APIView):
    def get(self, request):
        page = Events.objects.all()
        serializer = LandingPageSerializer(page, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)