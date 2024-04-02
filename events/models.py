from django.db import models
from django.core.validators import FileExtensionValidator
import uuid
from schools.models import *
from portals.base import BaseModel

# Create your models here.

class Event(BaseModel):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length = 20)
    title = models.CharField(max_length = 80)
    date = models.DateField(null = True, blank = True)
    time = models.TimeField(null=True, blank=True)
    location = models.TextField(null = True, blank = True)
    desc = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to="img/thumbnails", null=True, blank=True)
    videos = models.FileField(upload_to='videos/', validators=[FileExtensionValidator(['mp4', 'avi', 'mov', 'wmv', 'flv'])], null=True, blank=True)

    def _str_(self):
        return self.name
    

class EventImages(BaseModel):
    event = models.ForeignKey(Event, on_delete = models.CASCADE, )
    image = models.ImageField(upload_to="img", default=" ", validators=[FileExtensionValidator
            (['jpg', 'jpeg', 'png'])], null=True, blank=True)
    
    def __str__(self):
        return f"Image for {self.event.name}"
    
class EventSpeaker(BaseModel):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="speaker_images/") 
    desc = models.TextField(null= True, blank=True)

    def __str__(self):
        return f"{self.name} at {self.id}"


