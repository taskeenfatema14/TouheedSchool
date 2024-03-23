from django.contrib import admin
from .models import *

# Register your models here.

########################################### EVENT #########################################################

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['id', 'event_name', 'event_title', 'event_date', 'event_time', 'event_location']

########################################### EVENT IMAGES ##################################################

@admin.register(EventImages)
class EventImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'event_name', 'image']

    def event_name(self, obj):
        return obj.event.event_name  
    
    event_name.short_description = 'Event Name'

########################################### EVENT SPEAKER #################################################

@admin.register(EventSpeaker)
class EventSpeakerAdmin(admin.ModelAdmin):
    list_display = ['id', 'speaker_name', 'speaker_image', 'speaker_desc', 'events']  

###########################################################################################################
