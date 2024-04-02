from django.urls import path

from .views import * 

urlpatterns = [
    path('events-np/',EventView.as_view(), name = 'events-np'),
    path('events-np/<str:id>/',EventView.as_view(), name = 'events-np'),
    path('speaker-card/',EventSpeakersCard.as_view(), name = 'speaker-card'),
    path('speaker-card/<str:id>/',EventSpeakersCard.as_view(), name = 'speaker-card'),
    path('create-event/', EventCreateAPIView.as_view(), name='create-event'),

]