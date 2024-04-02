from django.contrib import admin
from .models import *
from typing import Set

# Register your models here.

# admin.site.register(User)
    
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email','is_superuser', 'is_staff'] 
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        disabled_fields = set()  # type: Set[str]

        if not is_superuser:
            disabled_fields |= {
                'username',
                'is_superuser',
            }

        for f in disabled_fields:
            if f in form.base_fields:
                form.base_fields[f].disabled = True

        return form
