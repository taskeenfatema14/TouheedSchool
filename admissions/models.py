import uuid
from django.db import models
from schools.models import School
from portals.base import BaseModel

class Admission(BaseModel):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    step1 = models.TextField(blank=True, null=True)
    step2 = models.TextField(blank=True, null=True)
    documents_required = models.TextField(blank=True, null=True)
    fee_concession = models.TextField(blank=True, null=True)

    def __str__(self):
        return str(self.school)
