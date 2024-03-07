# from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from base.serializers import StaffSerializer
from base.models import Staff

@api_view(["GET"])
def get_staff_list(request):
    staff = Staff.objects.all()
    serializer = StaffSerializer(staff, many=True)
    return Response(serializer.data)
