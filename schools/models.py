from django.db import models
from django.core.validators import FileExtensionValidator
from portals.models import BaseModel
import uuid
from django.db import models
from portals.models import *
from PIL import Image
from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

############################################# School model ###############################################

class School(BaseModel):
    id         = models.UUIDField(default=uuid.uuid4,primary_key=True)
    name = models.CharField(max_length = 100)
    location = models.CharField(max_length = 100)
    image = models.ImageField(upload_to="school",blank=True,null=True,)
    video = models.FileField(upload_to="landing_page", blank=True, null=True, validators=[FileExtensionValidator(['mp4', 'avi', 'mov'])])
    facility = models.CharField(max_length = 100)
    description = models.TextField()
    principal = models.TextField(null = True, blank = True)
    contact_no = models.IntegerField()
    school_email      = models.EmailField(
        verbose_name = 'email_address',
        max_length=255,
        null = True,
        blank = True
    )

    def __str__(self):
        return self.name
    
########################################### CONTACT US ####################################################

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