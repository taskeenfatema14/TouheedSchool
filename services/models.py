# models.py
from django.db import models
import uuid
from portals.base import BaseModel
from schools.models import *

class Brochure(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pdf = models.FileField(upload_to='brochures')
    school = models.ForeignKey(School, on_delete=models.CASCADE)

    def __str__(self):
        return self.pdf.name
    
