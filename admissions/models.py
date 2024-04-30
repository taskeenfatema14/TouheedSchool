import uuid
from django.db import models
from schools.models import School
from portals.base import BaseModel
from django.core.exceptions import ValidationError

def validate_mobile_no(value):
    if len(value) != 10 or not value.isdigit():
        raise ValidationError('Mobile number must be 10 digits long and contain only digits.')

# class RegisterForm(BaseModel):
#     school = models.ForeignKey(School, on_delete=models.CASCADE)
#     student_name = models.CharField(max_length=100)
#     class_for_admission = models.CharField(max_length=50)
#     last_school_attended = models.CharField(max_length=100)
#     date_of_birth = models.DateField()
#     parents_name = models.CharField(max_length=100)
#     email_id = models.EmailField()
#     address = models.TextField()
#     mobile_no = models.CharField(max_length=10, validators=[validate_mobile_no])

#     def __str__(self):
#         return self.student_name

class Admission(BaseModel):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    step1 = models.TextField(blank=True, null=True)
    step2 = models.TextField(blank=True, null=True)
    documents_required = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.school)
