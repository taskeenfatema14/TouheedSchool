from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import *
from django.conf.urls.static import static 

urlpatterns = [
    path('user-view/',UserView.as_view(), name = 'all users'),
    path('user-view/<str:id>/',UserDetails.as_view(), name = 'all users'),
    path('login/',LoginAPIView.as_view(), name = 'login'),

    path('register/', RegisterUserApi.as_view()),
    path('forget-pwd/',ForgotPasswordApi.as_view(), name = 'forget-password'),
    path('verify-otp/',VerificationOtpApi.as_view(), name = 'verify-otp' ),
    path('set-pwd/',SetNewPasswordApi.as_view(), name = 'set-pwd'),
    path('change-password/', ChangePasswordApi.as_view(), name='change_password'),
]
