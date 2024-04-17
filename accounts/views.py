from rest_framework import generics
from .serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework import viewsets
from .permissions import *
from schools.serializers import SchoolSerializer
from .email import *
from .models import *
from django.http import Http404
from portals.services import generate_token
from portals.base import BaseAPIView

# Create your views here.

class UserView(APIView):
    # serializer_class = UserTRialSerializer
    # model = User
    # allowed_methods =  [GET, GETALL, POST, PUT, DELETE] 
    # related_models = {}

    def post(self, request):
        serializer = UserTrialSerializer(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
#     def get(self, request):
#         user = User.objects.all()
#         serializer = UserSerializer(user,many = True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
        
# class UserDetails(APIView):
#     def get_object(self, pk):
#         try:
#             return User.objects.get(pk=pk)
#         except User.DoesNotExist:
#             raise Http404

#     def get(self, request, pk):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         user = self.get_object(pk)
#         serializer = UserSerializer(user, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk):
#         user = self.get_object(pk)
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
    
class LoginAPIView(APIView):
    def post(self, request):
        email = request.data.get('email')  
        password = request.data.get('password')

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

class ForgotPasswordApi(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = ForgotPasswordSerializer(data=data)
            if serializer.is_valid():
                send_otp_via_email(serializer.validated_data['email'])

                return Response({
                    'status': 200,
                    'message': 'OTP sent successfully.',
                    'data': serializer.validated_data,
                })

            return Response({
                'status': 400,
                'message': 'Something went wrong',
                'data': serializer.errors
            })

        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Internal Server Error',
                'data': str(e),
            })
        
class VerificationOtpApi(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = VerifyForgotOTPSerializer(data=data)

            if serializer.is_valid():
                return Response({
                    'status': 200,
                    'message': 'OTP verification successful.',
                    'data': serializer.validated_data,
                })

            return Response({
                'status': 400,
                'message': 'OTP verification failed',
                'data': serializer.errors
            })

        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Internal Server Error',
                'data': str(e),
            })
        
class SetNewPasswordApi(APIView):
    def post(self, request):
        try:
            data = request.data
            serializer = SetNewPasswordSerializer(data=data)

            if serializer.is_valid():
                serializer.save()
                return Response({
                    'status': 200,
                    'message': 'Password reset successful.',
                    'data': serializer.validated_data,
                })

            return Response({
                'status': 400,
                'message': 'Password reset failed.',
                'data': serializer.errors
            })

        except Exception as e:
            print(e)
            return Response({
                'status': 500,
                'message': 'Internal Server Error',
                'data': str(e),
            })

# Not working
        
class ChangePasswordApi(APIView):
    def post(self,request,*args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data,context={'request': self.request})
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "Password updated successfully"},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [SchoolPermission]