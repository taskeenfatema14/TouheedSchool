from django.urls import path

from .views import * 

urlpatterns = [
    path('events-np/',EventAPIView.as_view(), name = 'events-np'),
    path('events-np/<str:id>/',EventView.as_view(), name = 'events-np'), #Home/Event
    path('events-details/',EventDetails.as_view(), name = 'events-details'), #Event Details(Particular School)
    path('speaker-card/',EventSpeakersCard.as_view(), name = 'speaker-card'),
    path('speaker-card/<str:id>/',EventSpeakersCard.as_view(), name = 'speaker-card'),
]