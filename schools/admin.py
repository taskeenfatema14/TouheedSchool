from django.contrib import admin
from .models import *
from django.core.exceptions import ObjectDoesNotExist

class SchoolAdmin(admin.ModelAdmin):
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
                # Superusers can always add schools
                return True
            else:
                # Check if the user has a school associated with them
                try:
                    return request.user.school is None
                except ObjectDoesNotExist:
                    return False
        return super().has_add_permission(request)

# Register the SchoolAdmin class with the School model
admin.site.register(School, SchoolAdmin)
admin.site.register(Infrastructure)


# admin.site.register(School)


