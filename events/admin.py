from django.contrib import admin
from schools.models import *
from events.models import *
from .models import *

class EventImagesInline(admin.TabularInline):
    model = EventImages
    extra = 1
    # classes = ['collapse'] 

    def has_delete_permission(self, request, obj=None):
        return False
    
class EventSpeakerInline(admin.TabularInline):
    model = EventSpeaker
    extra = 1
    # classes = ['collapse'] 

    def has_delete_permission(self, request, obj=None):
        return False

class EventAdmin(admin.ModelAdmin):
    inlines = [EventImagesInline, EventSpeakerInline]
    list_display = ['id', 'name', 'title', 'date', 'time', 'location']
    
admin.site.register(Event, EventAdmin)
