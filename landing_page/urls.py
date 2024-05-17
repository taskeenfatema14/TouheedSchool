from django.urls import path
from .views import *

urlpatterns = [
    path('school/<str:id>', LandingPageSchool.as_view(), name='landing-pg-school'),
    path('latest-events/', LatestEvents.as_view(), name = 'latest-events'),
    path('our-best-features/',InfrastructureAPI.as_view(), name = 'our-best-features'),
    path('testimonials/',Testimonials.as_view(), name = 'testimonials'),
    path('school-events/<str:id>', SchoolEventsAPI.as_view(), name='school-events-api'),
    path('about-us-lp/',AboutUsLP.as_view(), name = 'about-us'),
    path('best-campus/',GalleryView.as_view(), name = 'best-campus'),
    # path('landing-pg-detail/',LandingPageDetail.as_view(), name = 'landing-pg-detail')
]