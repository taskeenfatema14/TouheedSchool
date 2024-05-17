from django.contrib import admin
from .models import *
from typing import Set


class CustomUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if 'password' in form.cleaned_data:
            password = form.cleaned_data['password']
            obj.set_password(password)
        super().save_model(request, obj, form, change)

    def display_school(self, requset, obj):
        if obj.school():
            return obj.school.name()
    
admin.site.register(User, CustomUserAdmin)

# class CustomUserAdmin(UserAdmin):
#     list_display = ('email', 'name', 'is_superuser', 'get_school_name', 'last_login')
#     list_filter = ('is_superuser',)
#     search_fields = ('email', 'name')
#     ordering = ('email',)

#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         print(qs)
#         if request.user.is_superuser:
#             return qs
#         return qs.filter(school=request.user.school)
        

#     def get_school_name(self, obj):
#         if obj.school:
#             return obj.school.name
#         return None
#     get_school_name.short_description = 'School'
    

# admin.site.register(User, CustomUserAdmin)
