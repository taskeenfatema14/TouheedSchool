from django.urls import path
from .views import *

urlpatterns = [
    path('events-np/',EventView.as_view(), name = 'all events'),
    path('events-pk/<str:pk>/',EventDetail.as_view(), name = 'single event'),
    path('speaker-card/',EventSpeakersCard.as_view(), name = 'speaker-card'),
    path('speaker-card/<int:pk>/'   ,EventSpeakersCard.as_view(), name = 'speaker-card')
]