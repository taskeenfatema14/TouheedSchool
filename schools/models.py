from django.db import models
from django.core.validators import FileExtensionValidator
from portals.models import BaseModel

# Create your models here.

class School(BaseModel):
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="schoolImage", blank=True, null=True)
    video = models.FileField(upload_to="landing_page", blank=True, null=True, validators=[FileExtensionValidator(['mp4', 'avi', 'mov'])])
    facility = models.CharField(max_length = 100)
    description = models.TextField()
    principle = models.TextField()
    contact_no = models.IntegerField()

class Events(models.Model):
    school = models.ForeignKey(School, related_name='events', on_delete=models.CASCADE)
    event_name = models.CharField(max_length = 20)
    event_title = models.CharField(max_length = 80)
    event_date = models.DateField(null = True, blank = True)
    event_time = models.TimeField(null=True, blank=True)
    event_location = models.TextField(null = True, blank = True)
    event_desc = models.TextField(null=True, blank=True)
    event_image = models.ImageField(upload_to ='images/', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    event_videos = models.FileField(upload_to='videos/', validators=[FileExtensionValidator(['mp4', 'avi', 'mov', 'wmv', 'flv'])], null=True, blank=True)
    
    def __str__(self):
        return self.event_name
    
class EventSpeaker(models.Model):
    events = models.ForeignKey('Events', related_name='event_speakers', on_delete=models.CASCADE)
    speaker_name = models.CharField(max_length=50)
    speaker_image = models.ImageField(upload_to='images/', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    speaker_desc = models.TextField(max_length = 100)

    def __str__(self):
        return self.speaker_name


