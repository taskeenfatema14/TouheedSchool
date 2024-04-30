from django.contrib import admin
from .models import *

# class AdmissionsAdmin(admin.TabularInline):
#     model = Admission

# class RegisterAdmin(admin.ModelAdmin):
#     inlines =[AdmissionsAdmin]
# admin.site.register(RegisterForm)
admin.site.register(Admission)
# admin.site.register(RegisterForm, RegisterAdmin)
# admin.site.register(Admission, AdmissionsAdmin)

# from django.contrib import admin
# from schools.models import *
# from .models import *

# class RegisterFormInline(admin.TabularInline):
#     model = RegisterForm

#     def has_delete_permission(self, request, obj=None):
#         return False

# class RegisterFormAdmin(admin.ModelAdmin):
#     inlines = [RegisterFormInline]
#     # list_display = ('id', 'student_name')

# admin.site.register(RegisterForm, RegisterFormAdmin)

# class AdmissionInline(admin.TabularInline):
#     model = Admission

#     def has_delete_permission(self, request, obj=None):
#         return False
    
# class AdmissionAdmin(admin.ModelAdmin):
#     inlines = [AdmissionInline]
#     # list_display = ('id', 'school', 'description')

# admin.site.register(Admission, AdmissionAdmin)

###################

# class RegisterFormAdmin(admin.ModelAdmin):
#     model = RegisterForm
#     list_display = ('id', 'student_name')

# admin.site.register(RegisterForm, RegisterFormAdmin)

# class RegisterFormInline(admin.TabularInline):
#     model = RegisterForm
#     extra = 1  # Number of extra forms to show

# class AdmissionAdmin(admin.ModelAdmin):
#     model = Admission
#     inlines = [RegisterFormInline]
#     list_display = ('id', 'school', 'description')

# admin.site.register(Admission, AdmissionAdmin)