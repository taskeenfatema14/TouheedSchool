from django.urls import path
from .views import *

urlpatterns = [

    path('school/', SchoolApi.as_view()),
    path('productput/<uuid:id>/', SchoolPutDeleteApi.as_view(), name='category-detail'),

    path('school', SchoolApi.as_view()),
    path('schoolput/<uuid:id>/', SchoolPutDeleteApi.as_view(), name='category-detail'),
    # path('schoolpagination/', SchoolApiPagination.as_view()),

    # path('schooltrial/<uuid:id>/', SchoolApi.as_view()),
    # path('schooltrial/', SchoolApi.as_view()),

    path('contactus/', ContactUsApi.as_view()),
    path('contactusall/', ContactUsAll.as_view()),

    # path('landingpage/', LandingPageApi.as_view()),

    # path('infrastructure/', InfrastructureAPI.as_view()),
    # path('infrastructure/<uuid:id>', InfrastructureAPI.as_view()),
    

    # path('contactus/', ContactUsApi.as_view()),
    # path('contactusall/', ContactUsAll.as_view()),
    
]
