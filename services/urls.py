# urls.py
from django.urls import path
from .views import DownloadPDFView

urlpatterns = [
    path('download_pdf/<uuid:uuid>/', DownloadPDFView.as_view(), name='download-pdf'),
]
