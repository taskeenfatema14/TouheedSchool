from django.urls import path
<<<<<<< HEAD
from .views import * 

=======
from .views import *
>>>>>>> 749970f3ea87b628f1a409a0234452924fd0221f

urlpatterns = [

    path('school/', SchoolApi.as_view()),
    path('productput/<uuid:id>/', SchoolPutDeleteApi.as_view(), name='category-detail'),

    path('school', SchoolApi.as_view()),
    path('schoolput/<uuid:id>/', SchoolPutDeleteApi.as_view(), name='category-detail'),
    path('schoolpagination/', SchoolApiPagination.as_view()),

<<<<<<< HEAD
    path('schooltrial/<uuid:id>/', SchoolgetAPI.as_view()),
    path('schooltrial/', SchoolgetAPI.as_view()),


    path('contactus/', ContactUsApi.as_view()),
    path('contactusall/', ContactUsAll.as_view()),

    path('landingpage/', LandingPageApi.as_view()),

    path('infrastructure/', InfrastructureAPI.as_view()),
    path('infrastructure/<uuid:id>', InfrastructureAPI.as_view()),
    

    
=======
    path('contactus/', ContactUsApi.as_view()),
    path('contactusall/', ContactUsAll.as_view()),
>>>>>>> 749970f3ea87b628f1a409a0234452924fd0221f
]