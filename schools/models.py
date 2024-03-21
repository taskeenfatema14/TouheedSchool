from django.db import models
from portals.models import *
from PIL import Image
from django.core.validators import FileExtensionValidator
from django.core.validators import FileExtensionValidator
from portals.models import BaseModel


from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.


############   KOMAL    #######################
    

class EventSpeaker(models.Model):
    events = models.ForeignKey('Events', related_name='event_speakers', on_delete=models.CASCADE)
    speaker_name = models.CharField(max_length=50)
    speaker_image = models.ImageField(upload_to='images/', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])])
    speaker_desc = models.TextField(max_length = 100)

    def __str__(self):
        return self.speaker_name


##############################   MY CODE    #################################################################
# class Image(models.Model):
#     image = models.ImageField(upload_to="schoolImages", blank=True, null=True) 
    
class School(BaseModel):
    id         = models.UUIDField(default=uuid.uuid4,primary_key=True)
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="school",blank=True,null=True,)
    video = models.FileField(upload_to="landing_page", blank=True, null=True, validators=[FileExtensionValidator(['mp4', 'avi', 'mov'])])
    facility = models.CharField(max_length = 100)
    description = models.TextField()
    principle = models.TextField()
    contact_no = models.IntegerField()
    school_email      = models.EmailField(
        verbose_name = 'email_address',
        max_length=255,
    )

    
class ContactUs(BaseModel):
    school     = models.ForeignKey(School, on_delete=models.CASCADE, related_name='contact_us',)
    user_email      = models.EmailField(
        verbose_name = 'email_address',
        max_length=255,
    )
    full_name  = models.CharField(max_length=100)
    subject    = models.CharField(max_length=50)
    message    = models.CharField(max_length=100)

@receiver(post_save, sender=ContactUs)
def send_contact_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Contact Us'
        message = 'Thank you for contacting us. We will get back to you soon.'
        email_from = settings.EMAIL_HOST
        send_mail(subject, message, email_from, [instance.user_email], fail_silently=False)

        # Sending email to school
        school_email = instance.school.school_email  # Assuming 'email' is the field name storing the email address in the School model
        school_subject = 'New Contact Inquiry'
        school_message = f'A new contact inquiry has been received from {instance.full_name}.'
        send_mail(school_subject, school_message, email_from, [school_email], fail_silently=False)


class Events(models.Model):
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
    

class EventImages(models.Model):
    event = models.ForeignKey(Events, on_delete = models.CASCADE, related_name = "images")
    image = models.ImageField(upload_to="img", default=" ", validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])], null=True, blank=True)
    
    def _str_(self):
        return f"Image for {self.event.event_name}"