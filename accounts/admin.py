from django.contrib import admin
from .models import *
from typing import Set

class CustomUserAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        print("Inside save_model method") 
        obj.user = request.user
        obj.save()

    def get_queryset(self, request): 
        # qs = super().get_queryset(request)  
        # return qs.filter(user=request.user)
        print("Inside get_queryset method")
        qs = super().get_queryset(request)  
        print(qs)
        if request.user.is_superuser:
            return qs  # Superuser can see all data
        elif hasattr(request.user, 'school'):  # Check if the user has a school associated
            return qs.filter(school=request.user.school)
        # If the user is not a superuser and does not have a school, they can't see any data
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

# class FilterUserAdmin(UserAdmin):
#     list_display = ('email', 'name', 'school', 'is_staff', 'is_superuser')
#     list_filter = ('is_staff', 'is_superuser')
#     search_fields = ('email', 'name')
#     readonly_fields = ('date_joined',)
#     ordering = ('email',) 

#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if not request.user.is_superuser:
#             # Filter queryset based on the currently logged-in user's associated school
#             qs = qs.filter(school=request.user.school)
#             print(qs)
#         return qs
    

    #     return form
    
admin.site.register(User, CustomUserAdmin)
