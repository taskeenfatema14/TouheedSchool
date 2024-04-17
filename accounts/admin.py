from django.contrib import admin
from .models import *
from typing import Set
    
# Password is being hashed when adding user from admin panel

class CustomUserAdmin(admin.ModelAdmin):
    # def save_model(self, request, obj, form, change):
    #     if 'password' in form.cleaned_data:
    #         password = form.cleaned_data['password']
    #         obj.set_password(password)
    #     super().save_model(request, obj, form, change)

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

admin.site.register(User, CustomUserAdmin)