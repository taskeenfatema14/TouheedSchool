from django.db import models
from django.db.models.fields import NullBooleanField
from tinymce.models import HTMLField
from PIL import Image

# Create your models here.

# *********************************** EVENT MODEL *********************************** 
class Event(models.Model):
    event_title = models.TextField(null=False,blank=False)
    event_desc = HTMLField(null=True,blank=True)
    event_date = models.DateTimeField(null=True,blank=True)
    event_location = models.TextField(default = "Gangolli - karnataka.", null=True,blank=True)
    event_image = models.ImageField(upload_to='images/event/thumbnail/', null=True, blank=True, help_text="Best Image Resolution width: 580 x Height: 565")
    # event_image = ResizedImageField(size=[853, 853], quality=75, upload_to='images/')
    
    def __str__(self):
        return self.event_title

    def save(self, *args, **kwargs):
        super(Event, self).save(*args, **kwargs)
        image = Image.open(self.event_image)
        (width, height) = image.size     
        size = (580, 565)
        image = image.resize(size, Image.LANCZOS )
        image.save(self.event_image.path)
            
    class Meta:
        ordering = ["-pk"]
        verbose_name = "Event"
        verbose_name_plural = "All Event"

class EventImages(models.Model):
    event = models.ForeignKey(Event, default=None, on_delete=models.CASCADE)
    images = models.ImageField(upload_to="images/event/banner/", null=True, blank=True, help_text="Best Image Resolution width: 1280 x Height: 720")

    def __str__(self):
        return self.event.event_title
    
    def save(self, *args, **kwargs):
        super(EventImages, self).save(*args, **kwargs)
        image = Image.open(self.images)
        (width, height) = image.size  
        size = (1280, 720)
        image = image.resize(size, Image.LANCZOS )
        image.save(self.images.path)

    
# *********************************** EVENT MODEL *********************************** 

class Staff(models.Model):
    person_name = models.TextField(null=False, blank=False)
    person_title = models.TextField(null=True, blank=True)
    person_occupation = models.TextField(null=True, blank=True)
    person_image = models.ImageField(upload_to="images/staff/", null=True, blank=True, help_text="Best Image Resolution width: 640 x Height: 825")

    def __str__(self):
        return self.person_name

    def save(self, *args, **kwargs):
        super(Staff, self).save(*args,**kwargs)
        image = Image.open(self.person_image)
        (width, height ) = image.size
        size = (640, 825)
        image = image.resize(size, Image.LANCZOS)
        image.save(self.person_image.path)

    class Meta:
        ordering = ["-pk"]
        verbose_name = "Staff"
        verbose_name_plural = "All Staff"


class MailLog(models.Model):
    mFrom = models.TextField(verbose_name="Mail From")
    to = models.TextField(verbose_name="Mail To")
    subject = models.TextField(verbose_name="Subject")
    body = models.TextField(verbose_name="Mail Body")
    sent_at = models.DateTimeField(auto_now_add=True, verbose_name="Sent On")
    queue = models.BooleanField(verbose_name="Queued", default=True)

    def __str__(self):
        return self.to

    class Meta:
        ordering = ["-pk"]
        verbose_name = "Mail"
        verbose_name_plural = "All Mails"


