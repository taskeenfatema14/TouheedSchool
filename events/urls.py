from django.urls import path
from .views import *

urlpatterns = [
    path('events/',EventView.as_view(), name = 'all events'),
    path('event-detail/<str:pk>/',EventDetail.as_view(), name = 'single event'),
    path('full-details/<str:pk>/',EventFullDetail.as_view(), name = 'details'),
    path('speaker-card/',EventSpeakersCard.as_view(), name = 'speaker-card'),
    path('speaker-card/<int:pk>/'   ,EventSpeakersCard.as_view(), name = 'speaker-card')
]