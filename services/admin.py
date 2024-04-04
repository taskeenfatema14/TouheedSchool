# admin.py

from django.contrib import admin
from .models import Brochure

@admin.register(Brochure)
class BrochureAdmin(admin.ModelAdmin):
    list_display = ['id', 'pdf', 'created_on', 'updated_on']
    search_fields = ['pdf__name']
