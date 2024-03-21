from django.urls import path
from .views import * 


urlpatterns = [

    path('school/', SchoolApi.as_view()),
    path('productput/<uuid:id>/', SchoolPutDeleteApi.as_view(), name='category-detail'),
    path('events/',EventView.as_view(), name = 'all events'),
    path('event-detail/<int:pk>/',EventDetail.as_view(), name = 'single event'),
    path('full-details/<int:pk>/',EventFullDetail.as_view(), name = 'details'),
    path('speaker-card/',EventSpeakersCard.as_view(), name = 'speaker-card'),
    path('speaker-card/<int:pk>/'   ,EventSpeakersCard.as_view(), name = 'speaker-card'),


    path('school', SchoolApi.as_view()),
    path('schoolput/<uuid:id>/', SchoolPutDeleteApi.as_view(), name='category-detail'),
    path('schoolpagination/', SchoolApiPagination.as_view()),

    path('contactus/', ContactUsApi.as_view()),
    path('contactusall/', ContactUsAll.as_view()),

    path('landingpage/', LandingPageApi.as_view()),
    

    
]