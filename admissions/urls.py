from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterFormAPIView.as_view(), name='registerform-create'),
    path('information/', AdmissionsAPIView.as_view(), name='admission-list'),
    path('school_info/<uuid:id>/', AdmissionAPIView.as_view(), name='admission-detail'),
]