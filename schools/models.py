from django.db import models
from django.utils import timezone
from portals.models import *
from PIL import Image
from django.core.validators import FileExtensionValidator
from portals.base import BaseModel
from portals.models import BaseModel
from django.core.mail import send_mail
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db import models
import uuid


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
    principal = models.TextField(null = True, blank = True)
    contact_no = models.IntegerField()
    school_email      = models.EmailField(
        verbose_name = 'email_address',
        max_length=255,
    )


class Event(BaseModel):
    event_title = models.TextField(null=False,blank=False)
    event_desc = models.TextField(null=True,blank=True)
    event_date = models.DateTimeField(null=True,blank=True)
    event_location = models.TextField(default = "Gangolli - karnataka.", null=True,blank=True)
    event_image = models.ImageField(upload_to='images/event/thumbnail/', null=True, blank=True, help_text="Best Image Resolution width: 580 x Height: 565")
    # event_image = ResizedImageField(size=[853, 853], quality=75, upload_to='images/')
    school = models.ForeignKey(School, on_delete=models.CASCADE, null=True, blank=True)
    
class ContactUs(BaseModel):
    school     = models.ForeignKey(School, on_delete=models.CASCADE)
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


class Infrastructure(BaseModel):
    school     = models.ForeignKey(School, on_delete=models.CASCADE, related_name='infrastructure',)
    image      = models.ImageField(upload_to="infrastructure",blank=True,null=True,)
    title      = models.CharField(max_length=100)


class FrequentlyAskedQuestions(BaseModel):
    questions = models.CharField(max_length=300)
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="questions")
    answer  = models.CharField(max_length=300)


class QuestionAnswer(BaseModel):
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name="answers")




    #     null = True,
    #     blank = True
    # )

    def __str__(self):
        return self.name
    
########################################### CONTACT US ####################################################

class ContactUs(BaseModel):
    school     = models.ForeignKey(School, on_delete=models.CASCADE)
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
class MailLog(models.Model):
    mail_id = models.AutoField(primary_key=True)
    mFrom = models.EmailField()
    to = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    queue = models.CharField(max_length=50)
    school = models.ForeignKey(School, on_delete=models.CASCADE)  # Add foreign key field to associate each mail log with a school
    principal = models.EmailField()  # Add field to store the email address of the principal

    def __str__(self):
        return f"Mail ID: {self.mail_id}, From: {self.mFrom}, To: {self.to}, Subject: {self.subject}"


