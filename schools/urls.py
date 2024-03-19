from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from .views import *
from django.conf.urls.static import static 
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('school/', SchoolApi.as_view()),
    path('productput/<uuid:id>/', SchoolPutDeleteApi.as_view(), name='category-detail'),
    path('events/',EventView.as_view(), name = 'all events'),
    path('event-detail/<str:pk>/',EventDetail.as_view(), name = 'single event'),
    path('full-details/<str:pk>/',EventFullDetail.as_view(), name = 'details'),
    path('speaker-card/',EventSpeakersCard.as_view(), name = 'speaker-card'),
    path('speaker-card/<int:pk>/'   ,EventSpeakersCard.as_view(), name = 'speaker-card')
]