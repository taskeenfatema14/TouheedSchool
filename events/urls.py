from django.urls import path

from .views import * 

urlpatterns = [
    path('events-np/',EventView.as_view(), name = 'all events'),
    path('event-detail/<uuid:pk>/',EventDetail.as_view(), name = 'single event'),
    # path('full-details/<int:pk>/',EventFullDetail.as_view(), name = 'details'),
    path('speaker-card/',EventSpeakersCard.as_view(), name = 'speaker-card'),
    path('speaker-card-pk/<uuid:pk>/',EventSpeakersCardPK.as_view(), name = 'speaker-card'),
]