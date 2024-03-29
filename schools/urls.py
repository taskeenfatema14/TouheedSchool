from django.urls import path
from .views import *

urlpatterns = [

    path('school-getpost/', SchoolApi.as_view()),
    path('product-putdelete/<uuid:id>/', SchoolPutDeleteApi.as_view(), name='category-detail'),

    # path('school', SchoolApi.as_view()),
    # path('schoolput/<uuid:id>/', SchoolPutDeleteApi.as_view(), name='category-detail'),
    path('schoolpagination/', SchoolApiPagination.as_view()),

    # path('schooltrial/<uuid:id>/', SchoolApi.as_view()),
    # path('schooltrial/', SchoolApi.as_view()),


    path('contactus/', ContactUsApi.as_view()),
    path('contactusall/', ContactUsAll.as_view()),

    # path('landingpage/', LandingPageApi.as_view()),

    path('infrastructure/', InfrastructureAPI.as_view()),
    path('infrastructure/<uuid:id>', InfrastructureAPI.as_view()),
    path('infra-pagination/', InfrastructurePaginationApi.as_view()),

    path('faq/', FaqApi.as_view()),
    path('faq/<uuid:id>/', FaqApi.as_view()),
    
]
