from django.contrib import admin

# Register your models here.

from .models import Event,EventImages,MailLog,Staff

class EventImagesAdmin(admin.StackedInline):
    model = EventImages

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['event_title', 'event_desc']
    list_filter = []
    search_fields = ['event_title']
    inlines = [EventImagesAdmin]


@admin.register(MailLog)
class MailLogAdmin(admin.ModelAdmin):
    list_display = ('sent_at','mFrom','to','queue',)
    list_filter = ("queue",)
    search_fields = ("to",)

@admin.register(Staff)
class StaffAdmin(admin.ModelAdmin):
    list_display = ('person_name','person_title',)
    list_filter = ()
    search_fields = ('person_name','person_title','person_occupation',)