from django.urls import path

from .views import * 

urlpatterns = [
    path('events-list/',EventAPIView.as_view(), name = 'events-list'), #List of Events with all fields
    path('events-list/<str:id>',EventAPIView.as_view(), name = 'events-list'), #List of Events with all fields
    path('events-np/<str:id>/',EventView.as_view(), name = 'events-np'), #Home/Event
    path('events-details/',EventDetails.as_view(), name = 'events-details'), #Event Details(Particular School)
]