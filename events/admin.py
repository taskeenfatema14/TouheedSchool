from django.contrib import admin
from schools.models import *
from events.models import *
from .models import *

# Register your models here.

@admin.register(Event)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'title', 'date', 'time', 'location']

@admin.register(EventSpeaker)
class EventSpeakerAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image', 'desc']  

@admin.register(EventImages)
class EventImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'image']

    def name(self, obj):
        return obj.event.name  
    
    name.short_description = 'Event Name'



