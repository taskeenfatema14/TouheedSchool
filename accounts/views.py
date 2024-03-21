from django.shortcuts import render
from rest_framework import generics
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
# Create your views here.

class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()  
    serializer_class = UserSerializer

class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all() 
    serializer_class = UserSerializer

class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')  # Use 'email' as the key
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        if user:
            return Response({
                'user_id': user.pk,
                'email': user.email,
                'message':'Successfully logged in'
            })
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

from portals.services import generate_token

class RegisterUserApi(APIView):
    def post(self,request,*args, **kwargs):
        try : 
            serializer = UserSerializer(data=request.data)
            
            if  serializer.is_valid():
                user = serializer.save()
                print(user.id)
                token = generate_token(user.email)
                return Response({"message" : "User Created Succefully" , "data" : UserSerializer(user).data , "token" : token},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e :
            return Response({"error" : True , "message" : str(e)},status=status.HTTP_400_BAD_REQUEST)
        

