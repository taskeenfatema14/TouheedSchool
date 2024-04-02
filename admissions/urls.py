from django.urls import path
from .views import AdmissionCreateAPIView

urlpatterns = [
    path('register/', AdmissionCreateAPIView.as_view(), name='admission-create'),
]