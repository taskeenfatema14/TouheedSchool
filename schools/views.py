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
