from django.contrib import admin
from .models import *

########################################### School Admin ##################################################

@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'location', 'facility', 'contact_no'] 

###########################################################################################################
