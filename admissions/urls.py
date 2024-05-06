from django.urls import path
from .views import *

urlpatterns = [
    path('information/', AdmissionsAPIView.as_view(), name='admission-list'),
    path('school_info/<uuid:school_id>/', AdmissionAPIView.as_view(), name='admission-detail'),
]