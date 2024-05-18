from django.urls import path

from .views import * 

urlpatterns = [
    path('events-list/<str:id>',EventAPIView.as_view(), name = 'events-list'), #List of Events with all fields
    path('events-np/<str:id>/',EventView.as_view(), name = 'events-np'), #Home/Event (it has pagination)
    path('events-details/',EventDetails.as_view(), name = 'events-details'), #Event Details(Particular School)
    path('single-event/<str:id>/', SingleEventDetail.as_view(), name='event-detail'), #Single Event details
    path('events-each-school/<str:id>/', EventsEachSchool.as_view(), name = 'events-per-school') # Home/Event for each school
]
