from django.urls import path
<<<<<<< HEAD
from .views import * 

urlpatterns = [
    path('events/',EventView.as_view(), name = 'all events'),
    path('event-detail/<int:pk>/',EventDetail.as_view(), name = 'single event'),
    path('full-details/<int:pk>/',EventFullDetail.as_view(), name = 'details'),
    path('speaker-card/',EventSpeakersCard.as_view(), name = 'speaker-card'),
    path('speaker-card/<int:pk>/'   ,EventSpeakersCard.as_view(), name = 'speaker-card'),
=======
from .views import *

urlpatterns = [
    path('events-np/',EventView.as_view(), name = 'all events'),
    path('events-pk/<str:pk>/',EventDetail.as_view(), name = 'single event'),
    path('speaker-card/',EventSpeakersCard.as_view(), name = 'speaker-card'),
    path('speaker-card/<int:pk>/'   ,EventSpeakersCard.as_view(), name = 'speaker-card')
>>>>>>> 749970f3ea87b628f1a409a0234452924fd0221f
]