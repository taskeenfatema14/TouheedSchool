from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import Http404
from .models import *
from .serializers import *

class RegisterFormAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = RegisterFormSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
###################################Admission#############################################
    
class AdmissionsAPIView(APIView):
    def get(self, request):
        try:
            queryset = Admission.objects.all()
            serializer = AdmissionSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class AdmissionAPIView(APIView):
    def get_object(self, id):
        try:
            return Admission.objects.get(id=id)
        except Admission.DoesNotExist:
            raise Http404
        
    def get(self, request, id):
        try:
            admission = self.get_object(id)
            serializer = AdmissionSerializer(admission)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Http404:
            return Response({'error': 'Admission not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
