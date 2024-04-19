from django.contrib import admin
from .models import *
from typing import Set
from django.contrib.auth.admin import UserAdmin 
    
# Password is being hashed when adding user from admin panel

# class CustomUserAdmin(admin.ModelAdmin):
#     def save_model(self, request, obj, form, change):
#         if 'password' in form.cleaned_data:
#             password = form.cleaned_data['password']
#             obj.set_password(password)
#         super().save_model(request, obj, form, change)

# admin.site.register(User, CustomUserAdmin)

class FilterUserAdmin(UserAdmin):
    list_display = ('email', 'name', 'school', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')
    search_fields = ('email', 'name')
    readonly_fields = ('date_joined',)
    ordering = ('email',) 

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            # Filter queryset based on the currently logged-in user's associated school
            qs = qs.filter(school=request.user.school)
            print(qs)
        return qs
    

    def has_change_permission(self, request, obj=None):
        if obj and not request.user.is_superuser:
            # Check if the user is trying to change their own profile
            return obj == request.user
        return super().has_change_permission(request, obj)

admin.site.register(User, FilterUserAdmin)