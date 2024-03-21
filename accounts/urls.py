from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import *
from django.conf.urls.static import static 

urlpatterns = [
    path('user-view/',UserView.as_view(), name = 'all users'),
    path('user-detail/<int:pk>/',UserDetails.as_view(), name = 'single user'),
    path('login/',LoginAPIView.as_view(), name = 'login'),

    path('register/', RegisterUserApi.as_view())
]