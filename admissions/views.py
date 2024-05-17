from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import *
from .serializers import *

# ###################################Admission#############################################
class AdmissionsAPIView(APIView):
    def get(self, request):
        try:
            queryset = Admission.objects.all()
            serializer = AdmissionSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class AdmissionAPIView(APIView):
    def get_admissions_by_school(self, school_id):
        return Admission.objects.filter(school_id=school_id)

    def get(self, request, school_id):
        try:
            admissions = self.get_admissions_by_school(school_id)
            serializer = AdmissionSerializer(admissions, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
            
