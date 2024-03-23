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
        email = request.data.get('email')  
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

######################################## Forget password ###############################################################

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

################################################# Verify OTP ###########################################################
        
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
        

######################################## SET NEW password ##############################################################
        
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

######################################## Change password #########################################################

# Not working
        
class ChangePasswordApi(APIView):
    def post(self,request,*args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data,context={'request': self.request})
        if serializer.is_valid():
            serializer.save()
            return Response({"Success": "Password updated successfully"},status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

######################################## RESTRICTING TO OTHER SCHOOLS ############################################

class SchoolViewSet(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [SchoolPermission]

##################################################################################################################