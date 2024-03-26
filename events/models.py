from django.db import models
from django.core.validators import FileExtensionValidator
import uuid
from schools.models import *
from portals.models import BaseModel

# Create your models here.

class Events(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    school = models.ForeignKey(School, related_name='events', on_delete=models.CASCADE)
    event_name = models.CharField(max_length = 20)
    event_title = models.CharField(max_length = 80)
    event_date = models.DateField(null = True, blank = True)
    event_time = models.TimeField(null=True, blank=True)
    event_location = models.TextField(null = True, blank = True)
    event_desc = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to="img/thumbnails", null=True, blank=True)
    event_videos = models.FileField(upload_to='videos/', validators=[FileExtensionValidator(['mp4', 'avi', 'mov', 'wmv', 'flv'])], null=True, blank=True)
    
    def _str_(self):
        return self.event_name
    

class EventImages(BaseModel):
    event = models.ForeignKey(Events, on_delete = models.CASCADE, related_name = "images")
    image = models.ImageField(upload_to="img", default=" ", validators=[FileExtensionValidator
            (['jpg', 'jpeg', 'png'])], null=True, blank=True)
    
    def __str__(self):
        return f"Image for {self.event.event_name}"
    
class EventSpeaker(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, default = " "),
    speaker_name = models.CharField(max_length=100)
    speaker_image = models.URLField()
    speaker_desc = models.TextField()

    def __str__(self):
        return f"{self.speaker_name} at {self.event}"