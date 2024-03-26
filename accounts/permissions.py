from rest_framework import permissions

class SchoolPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user can view all schools or has permission to CRUD own school
        return request.user.can_view_all_schools() or request.user.can_crud_own_school()

    def has_object_permission(self, request, view, obj):
        # Check if the user can view the school object or has permission to CRUD own school
        return request.user.can_view_school(obj) or request.user.can_crud_school(obj)