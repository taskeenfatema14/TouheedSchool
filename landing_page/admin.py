from django.contrib import admin
from .models import *
from inline_actions.admin import InlineActionsModelAdminMixin

# Register your models here.
admin.site.register(AboutUs)

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['id', 'image']

admin.site.register(Gallery, GalleryAdmin)