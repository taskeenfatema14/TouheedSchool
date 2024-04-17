from django.contrib import admin
from .models import *
from django.core.exceptions import ObjectDoesNotExist

from django.contrib import admin
from .models import *
class ContactUsInline(admin.TabularInline):
    model = ContactUs

class InfrastructureInline(admin.TabularInline):
    model = Infrastructure

class NoticeboardInline(admin.TabularInline):
    model = Noticeboard

class SchoolFAQInline(admin.TabularInline):
    model = FrequentlyAskedQuestion

class SchoolAdmin(admin.ModelAdmin):
    inlines = [ContactUsInline, InfrastructureInline, NoticeboardInline, SchoolFAQInline]    

    # Override methods as needed

class SchoolCUAdmin(admin.ModelAdmin):
    inlines =[ContactUsInline]

class SchoolInfraAdmin(admin.ModelAdmin):
    inlines =[InfrastructureInline]

admin.site.register(School, SchoolAdmin)
admin.site.register(FrequentlyAskedQuestion) #SchoolFaqAdmin


class SchoolFAQAdmin(admin.TabularInline):
    model = FrequentlyAskedQuestion

class SchoolFaqAdmin(admin.ModelAdmin):
    inlines =[SchoolFAQAdmin]

    # Override the has_change_permission method
    def has_change_permission(self, request, obj=None):
        if obj is not None and request.user.is_authenticated:
            # Check if the user has a school and if it matches the school being accessed
            try:
                if request.user.school and request.user.school == obj:
                    return True
            except ObjectDoesNotExist:
                pass
            return False
        return super().has_change_permission(request, obj=obj)

    # Override the has_delete_permission method
    def has_delete_permission(self, request, obj=None):
        if obj is not None and request.user.is_authenticated:
            # Check if the user has a school and if it matches the school being accessed
            try:
                if request.user.is_superuser:
                    return True  # Superusers can delete schools
                elif request.user.school and request.user.school == obj:
                    return True
            except ObjectDoesNotExist:
                pass
            return False
        return super().has_delete_permission(request, obj=obj)

    # Override the has_add_permission method
    def has_add_permission(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return True
            else:
                try:
                    return request.user.school is None
                except ObjectDoesNotExist:
                    return False
        return super().has_add_permission(request)
