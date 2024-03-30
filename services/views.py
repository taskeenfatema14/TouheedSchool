from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.conf import settings
from django.views.generic import View
from .models import Brochure

class DownloadPDFView(View):
    def get(self, request, uuid):
        brochure = get_object_or_404(Brochure, id=uuid)
        file_path = brochure.pdf.path

        with open(file_path, 'rb') as pdf_file:
            response = HttpResponse(pdf_file.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename=' + brochure.pdf.name
            return response

