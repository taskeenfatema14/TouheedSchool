# from rest_framework import generics, permissions
# from .models import School
# from .serializers import SchoolSerializer

# ################################ IsSuperuserOrIsSchoolStaff #########################################################

# class IsSuperuserOrIsSchoolStaff(permissions.BasePermission):
#     """
#     Custom permission to allow access only to superusers or staff associated with the school.
#     """

#     def has_permission(self, request, view):
#         if request.user.is_superuser:
#             return True  
#         if request.user.is_staff and request.method in permissions.SAFE_METHODS:
#             return True  
#         return False

#     def has_object_permission(self, request, view, obj):
#         if request.user.is_superuser:
#             return True
#         return obj.staff.filter(id=request.user.id).exists()

# ################################ SchoolListCreateAPIView #########################################################

# class SchoolListCreateAPIView(generics.ListCreateAPIView):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer
#     permission_classes = [IsSuperuserOrIsSchoolStaff]

#     def perform_create(self, serializer):
#         serializer.save(staff=[self.request.user])

# ################################ SchoolRetrieveUpdateDestroyAPIView #########################################################

# class SchoolRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = School.objects.all()
#     serializer_class = SchoolSerializer
#     permission_classes = [IsSuperuserOrIsSchoolStaff]

# ############################################################################################################################
