# models.py
from django.db import models
import uuid
from portals.base import BaseModel
from schools.models import *

class Brochure(BaseModel):
    school       = models.ForeignKey(School, on_delete=models.CASCADE)
    pdf          = models.FileField(upload_to='brochures')
    description  = models.TextField(null = True, blank= True)

    def __str__(self):
        return self.pdf.name
