from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.generic import View
from .models import Brochure

class DownloadPDFView(View):
    def get(self, request, uuid):
        try:
            brochure = get_object_or_404(Brochure, id=uuid)
            file_path = brochure.pdf.path
            content_type = 'application/pdf'  # Adjust content type as needed

            return JsonResponse({'file_path': file_path, 'content_type': content_type})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
