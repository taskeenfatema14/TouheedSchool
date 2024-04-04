from django.contrib import admin
from schools.models import *
from events.models import *
from .models import *

# Register your models here.

# @admin.register(Event)
# class EventsAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'title', 'date', 'time', 'location']

# @admin.register(EventSpeaker)
# class EventSpeakerAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'image', 'desc']  

# @admin.register(EventImages)
# class EventImagesAdmin(admin.ModelAdmin):
#     list_display = ['id', 'name', 'image']

#     def name(self, obj):
#         return obj.event.name  
    
#     name.short_description = 'Event Name'

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
