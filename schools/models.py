from django.db import models
from django.core.validators import FileExtensionValidator
from portals.models import BaseModel
import uuid

# Create your models here.

############################################# School model ###############################################

class School(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="schoolImage", blank=True, null=True)
    video = models.FileField(upload_to="landing_page", blank=True, null=True, validators=[FileExtensionValidator(['mp4', 'avi', 'mov'])])
    facility = models.CharField(max_length = 100)
    description = models.TextField()
    principal = models.TextField()
    contact_no = models.IntegerField()

    def __str__(self):
        return self.name
    
###########################################################################################################
