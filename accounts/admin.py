from django.contrib import admin
from .models import User

# Register your models here.

# admin.site.register(User)

# class CustomUserAdmin(admin.ModelAdmin):
#     def get_queryset(self, request):
#         qs = super().get_queryset(request)
#         if request.user.is_superuser:
#             return qs  
#         elif request.user.school:
#             return qs.filter(school=request.user.school)
#         else:
#             return qs.none()  

#     def get_form(self, request, obj=None, **kwargs):
#         form = super().get_form(request, obj, **kwargs)
#         if not request.user.is_superuser:
#             form.base_fields['school'].queryset = form.base_fields['school'].queryset.filter(pk=request.user.school.pk)
#             form.base_fields['school'].disabled = True
#         return form
    
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email','is_superuser', 'is_staff'] 