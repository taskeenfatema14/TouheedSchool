from rest_framework import generics, permissions
from .models import School
from .serializers import SchoolSerializer

class IsSuperuserOrIsSchoolStaff(permissions.BasePermission):
    """
    Custom permission to allow access only to superusers or staff associated with the school.
    """

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True  # Allow superusers unrestricted access
        if request.user.is_staff and request.method in permissions.SAFE_METHODS:
            return True  # Allow staff to read data
        return False

    def has_object_permission(self, request, view, obj):
        # Allow superusers unrestricted access
        if request.user.is_superuser:
            return True
        # Allow staff associated with the school to modify the school
        return obj.staff.filter(id=request.user.id).exists()


class SchoolListCreateAPIView(generics.ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsSuperuserOrIsSchoolStaff]

    def perform_create(self, serializer):
        # Associate the school with the staff creating it
        serializer.save(staff=[self.request.user])


class SchoolRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    permission_classes = [IsSuperuserOrIsSchoolStaff]
