from django.contrib import admin
from .models import *
from django.core.exceptions import ObjectDoesNotExist

class SchoolAdmin(admin.ModelAdmin):
    # Override the has_change_permission method
    def has_change_permission(self, request, obj=None):
        if obj is not None and request.user.is_authenticated:
            # Check if the user has a school and if it matches the school being accessed
            try:
                if request.user.school and request.user.school == obj:
                    return True
            except ObjectDoesNotExist:
                pass
            return False
        return super().has_change_permission(request, obj=obj)

    # Override the has_delete_permission method
    def has_delete_permission(self, request, obj=None):
        if obj is not None and request.user.is_authenticated:
            # Check if the user has a school and if it matches the school being accessed
            try:
                if request.user.is_superuser:
                    return True  # Superusers can delete schools
                elif request.user.school and request.user.school == obj:
                    return True
            except ObjectDoesNotExist:
                pass
            return False
        return super().has_delete_permission(request, obj=obj)

    # Override the has_add_permission method
    def has_add_permission(self, request):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return True
            else:
                try:
                    return request.user.school is None
                except ObjectDoesNotExist:
                    return False
        return super().has_add_permission(request)


# from accounts.models import User
# from django.contrib.auth.admin import UserAdmin
# from django.contrib.auth.models import Group, Permission


# class UserInline(admin.TabularInline):
#     model = User
#     extra = 0  # Control the number of empty forms displayed by default
# class SchoolAdmin(admin.ModelAdmin):
#     inlines = [UserInline]
#     list_display = ('name',)
#     search_fields = ('name',)

# # Customize User admin to display only the 'school' field for school admins
# class UserAdmin(admin.ModelAdmin):
#     list_display = ('email', 'name', 'is_superuser', )  
#     ordering = ('email',)  # Order by email (optional)
#     list_filter = ('is_superuser', 'is_staff')  # Filter by these fields (optional)
#     # ... other UserAdmin configuration options ...

# admin.site.register(User, UserAdmin)

# Register the SchoolAdmin class with the School model
admin.site.register(School, SchoolAdmin)
admin.site.register(Infrastructure)
admin.site.register(FrequentlyAskedQuestion)

# Notice Board Workinng ######################

class NoticeBoardImageInline(admin.TabularInline):
    model = NoticeboardImage
    extra = 1

class NoticeBoardAdmin(admin.ModelAdmin):
    inlines = [NoticeBoardImageInline]
    list_display = ['id','school', 'title']

admin.site.register(Noticeboard, NoticeBoardAdmin)

###############################

# # Get or create Django groups
# superuser_group, created = Group.objects.get_or_create(name='Superusers')
# school_admin_group, created = Group.objects.get_or_create(name='School Admins')

# # Assign superuser permissions (modify based on your requirements)
# superuser_group.permissions.set([
#     # Permission to add, change, and delete all models
#     perm for perm in Permission.objects.all()
# ])

# # Assign school admin permissions (modify based on your requirements)
# school_admin_group.permissions.set([
#     # Permission to add, change, and delete schools they own
#     perm for perm in Permission.objects.filter(content_type__app_label='schools', name__in=['add_school', 'change_school', 'delete_school'])
# ])