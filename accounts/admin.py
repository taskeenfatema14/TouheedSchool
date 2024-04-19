from django.contrib import admin
from .models import *
from typing import Set

class CustomUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        obj.user = request.user
        obj.save()

    def get_queryset(self, request): 
        # qs = super().get_queryset(request)  
        # return qs.filter(user=request.user)

        qs = super().get_queryset(request)  # For Django 1.6 and later
        if request.user.is_superuser:
            return qs  # Superuser can see all data
        elif hasattr(request.user, 'school'):  # Check if the user has a school associated
            return qs.filter(school=request.user.school)
        else:
            return qs.none()  

    def has_change_permission(self, request, obj=None):
        if not obj:
            return True  
        return obj.user == request.user  
    
    def save_model(self, request, obj, form, change):
        if 'password' in form.cleaned_data:
            password = form.cleaned_data['password']
            obj.set_password(password)
        super().save_model(request, obj, form, change)



    
    # def get_form(self, request, obj=None, **kwargs):
    #     form = super().get_form(request, obj, **kwargs)
    #     is_superuser = request.user.is_superuser
    #     disabled_fields = set()  # type: Set[str]

    #     if not is_superuser:
    #         disabled_fields |= {
    #             'username',
    #             'is_superuser',
    #         }

    #     for f in disabled_fields:
    #         if f in form.base_fields:
    #             form.base_fields[f].disabled = True

    #     return form
    
admin.site.register(User, CustomUserAdmin)