from django.contrib import admin
from .models import *

# admin.site.register(User)
# Register your models here.

# admin.site.register(User)
    
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['email','is_superuser', 'is_staff'] 
