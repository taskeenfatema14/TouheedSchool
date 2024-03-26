from django.contrib import admin
<<<<<<< HEAD
from schools.models import *
from events.models import *

=======
from .models import *

# Register your models here.

########################################### EVENT #########################################################
>>>>>>> 749970f3ea87b628f1a409a0234452924fd0221f

@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):
    list_display = ['id', 'event_name', 'event_title', 'event_date', 'event_time', 'event_location']

<<<<<<< HEAD
@admin.register(EventSpeaker)
class EventSpeakerAdmin(admin.ModelAdmin):
    list_display = ['id', 'speaker_name', 'speaker_image', 'speaker_desc', 'events']  

# @admin.register(School)
# class SchoolAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'location', 'facility', 'contact_no'] 
=======
########################################### EVENT IMAGES ##################################################
>>>>>>> 749970f3ea87b628f1a409a0234452924fd0221f

@admin.register(EventImages)
class EventImagesAdmin(admin.ModelAdmin):
    list_display = ['id', 'event_name', 'image']

    def event_name(self, obj):
        return obj.event.event_name  
    
    event_name.short_description = 'Event Name'

<<<<<<< HEAD
=======
########################################### EVENT SPEAKER #################################################

@admin.register(EventSpeaker)
class EventSpeakerAdmin(admin.ModelAdmin):
    list_display = ['id', 'speaker_name', 'speaker_image', 'speaker_desc', 'events']  

###########################################################################################################
>>>>>>> 749970f3ea87b628f1a409a0234452924fd0221f
