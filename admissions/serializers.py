from rest_framework import serializers
from .models import *

class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        exclude = ('created_on','updated_on','is_deleted')