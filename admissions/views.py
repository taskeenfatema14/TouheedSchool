from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Admission
from .serializers import AdmissionSerializer

class AdmissionCreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = AdmissionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
