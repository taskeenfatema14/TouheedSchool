from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate

# Create your views here.


############################################ USER(ADMIN & PRINCIPALS) ########################################################

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()  
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all() 
    serializer_class = UserSerializer


################################################### LOGIN #######################################################################
    
class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')  # Use 'email' as the key
        password = request.data.get('password')

        # Authenticate the user
        user = authenticate(request, email=email, password=password)

        if user:
            # If authentication successful, return user details
            return Response({
                'user_id': user.pk,
                'email': user.email,
                'name': user.name,  # Include any other fields you want to return
                'message': 'Successfully logged in'
            })
        else:
            # If authentication failed, return error message
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        

