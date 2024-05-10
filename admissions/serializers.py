from rest_framework import serializers
from .models import *

class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admission
        fields = ['id','school','description','step1','step2','documents_required','fee_concession']