from django.urls import path
from .views import *

urlpatterns = [
    path('landing-pg-school/', LandingPageSchool.as_view(), name='landing-pg-school'),
    path('latest-events/', LPLatestEvents.as_view(), name = 'latest-events'),
]