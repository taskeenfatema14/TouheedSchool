from django.urls import path
from .views import *

urlpatterns = [
    path('school/', SchoolApi.as_view()),
    path('productput/<uuid:id>/', SchoolPutDeleteApi.as_view(), name='category-detail'),
    path('landingpage/', LandingPageApi.as_view()),
    path('landing-school/', LandingPageSchools.as_view(), name = 'landing-page-school')
]