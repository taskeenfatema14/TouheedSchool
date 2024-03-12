from django.db import models
from portals.models import *
from PIL import Image
from django.core.validators import FileExtensionValidator

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

class Event(BaseModel):
    event_title = models.TextField(null=False,blank=False)
    event_desc = models.TextField(null=True,blank=True)
    event_date = models.DateTimeField(null=True,blank=True)
    event_location = models.TextField(default = "Gangolli - karnataka.", null=True,blank=True)
    event_image = models.ImageField(upload_to='images/event/thumbnail/', null=True, blank=True, help_text="Best Image Resolution width: 580 x Height: 565")
    # event_image = ResizedImageField(size=[853, 853], quality=75, upload_to='images/')
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='events', null=True, blank=True)
    
    def __str__(self):
        return self.event_title

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)
        image = Image.open(self.event_image)
        (width, height) = image.size     
        size = (580, 565)
        image = image.resize(size, Image.LANCZOS )
        image.save(self.event_image.path)    

    