# admin.py

from django.contrib import admin
from .models import Brochure

class BrochureAdmin(admin.ModelAdmin):
    list_display = ['id', 'pdf']

admin.site.register(Brochure)
