from django.urls import path
from .views import *

urlpatterns = [

    path('school-getpost/', SchoolApi.as_view(), name = 'school-getpost'),
    path('school-getpost/<str:id>', SchoolApi.as_view(), name = 'school-getpost'),

    path('contactus/', ContactUsApi.as_view()),
    # path('contactusall/', ContactUsAll.as_view()),

    path('infrastructure/', InfrastructureAPI.as_view()),
    path('infrastructure/<str:id>', InfrastructureAPI.as_view()),

    path('faq/<str:id>/', FaqApi.as_view()),
    path('faq/', FaqApi.as_view()),

    path('notice-board/', NoticeboardApi.as_view()),
    path('notice-board/<str:id>', NoticeboardApi.as_view()),

    path('schoolevent/', SchoolEventApi.as_view()),
    path('schoolevent/<str:id>', SchoolEventApi.as_view()),

    path('schooldetail/<str:id>', SchoolDetailAPiView.as_view()),

    path('about-us/<str:id>/', AboutUs.as_view()),
]
