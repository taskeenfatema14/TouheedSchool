from django.urls import path
from .views import *

urlpatterns = [
    path('landing-pg-school/<str:id>', LandingPageSchool.as_view(), name='landing-pg-school'),
    path('latest-events/', LatestEvents.as_view(), name = 'latest-events'),
    path('our-best-features/',InfrastructureAPI.as_view(), name = 'our-best-features'),
    path('testimonials/',Testimonials.as_view(), name = 'testimonials')
]