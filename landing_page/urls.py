from django.urls import path
from .views import *

urlpatterns = [
    path('landing-pg-school/', LandingPageSchool.as_view(), name='landing-pg-school'),
]