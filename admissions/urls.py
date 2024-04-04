from django.urls import path
from .views import *

urlpatterns = [
    path('register/', RegisterFormAPIView.as_view(), name='registerform-create'),
    path('admission_information/', AdmissionListAPIView.as_view(), name='admission-list'),
    path('school_info/<uuid:id>/', AdmissionFieldAPIView.as_view(), name='admission-detail'),
]