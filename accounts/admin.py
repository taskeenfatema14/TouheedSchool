from django.contrib import admin
from .models import *
from typing import Set

    
# Password is being hashed when adding user from admin panel

class CustomUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if 'password' in form.cleaned_data:
            password = form.cleaned_data['password']
            obj.set_password(password)
        super().save_model(request, obj, form, change)

admin.site.register(User, CustomUserAdmin)