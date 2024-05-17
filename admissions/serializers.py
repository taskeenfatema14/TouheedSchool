from rest_framework import serializers
from .models import *

class AdmissionSchool(serializers.ModelSerializer):
    class Meta:
        model  = School
        fields = ['name','logo'] 

class AdmissionSerializer(serializers.ModelSerializer):
    school_detail = AdmissionSchool(source='school')
    class Meta:
        model = Admission
        fields = ['id','school','description','step1','step2','documents_required','fee_concession','school_detail']