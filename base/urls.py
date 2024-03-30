from django.urls import path
from django.urls.conf import include

from rest_framework import routers
from .views import *
router = routers.DefaultRouter()
router.register('event',EventViewSet)


urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/',getUserProfile, name='users-profile'),
    path('event-list/',getEventList, name="get-event-list"),
    path('event-detail/<str:pk>/',get_event_detail, name="get_event_detail"),
    path('staff-list/',get_staff_list, name="get_staff_list"),




    path('',include(router.urls)),
    path('send-mail/', send_contact_mail, name="send_contact_mail")

]