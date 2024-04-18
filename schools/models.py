from django.db import models
from django.utils import timezone
from portals.models import *
from PIL import Image
from django.dispatch import receiver
from django.core.validators import FileExtensionValidator
from portals.base import BaseModel
from django.db import models
import uuid
from django.db.models.signals import post_save
from django.core.mail import send_mail
from core.settings import EMAIL_HOST_USER
from django.conf import settings
from django.db import transaction


class School(BaseModel):
    name              = models.CharField(max_length = 100)
    location          = models.CharField(max_length = 100)
    image             = models.ImageField(upload_to="school",blank=True,null=True,)
    video             = models.FileField(upload_to="landing_page", blank=True, null=True, validators=[FileExtensionValidator(['mp4', 'avi', 'mov'])])
    facility          = models.CharField(max_length = 100)
    description       = models.TextField()
    contact_no        = models.IntegerField()
    school_email      = models.EmailField(
        verbose_name  = 'email_address',
        max_length=255,
    )
    principal         = models.TextField(blank =True, null=True)
    summary           = models.TextField()
    logo              = models.ImageField(upload_to="school_logo",blank=True, null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if self.id:
            # If the instance already has an ID, it means it's already saved
            super().save(*args, **kwargs)
            return

        # If there's no existing record, save the new one and delete any existing logo
        try:
            with transaction.atomic():
                if School.objects.exists():
                    # Delete existing logo if it exists
                    existing_logo = School.objects.first().logo
                    if existing_logo:
                        existing_logo.delete()

                super().save(*args, **kwargs)
        except ValidationError as e:
            # Handle validation errors
            print("Validation Error:", e)
    
class ContactUs(BaseModel):
    school           = models.ForeignKey(School, on_delete=models.CASCADE,)
    user_email       = models.EmailField(
        verbose_name = 'email_address',
        max_length=255,
    )
    full_name        = models.CharField(max_length=100)
    subject          = models.CharField(max_length=50)
    message          = models.CharField(max_length=100)


class Infrastructure(BaseModel):
    school     = models.ForeignKey(School, on_delete=models.CASCADE, related_name='infrastructure')
    image      = models.ImageField(upload_to="infrastructure",blank=True,null=True,)
    title      = models.CharField(max_length=100)


class FrequentlyAskedQuestion(BaseModel):
    school     = models.ForeignKey(School, on_delete=models.CASCADE, related_name='frequentlyquestion_set',)
    question   = models.CharField(max_length=300, null=True)
    answer     = models.CharField(max_length=300,null=True)


class Noticeboard(BaseModel):
    school     = models.ForeignKey(School, on_delete=models.CASCADE, related_name='notice_board_set')
    title      = models.CharField(max_length=100, null=True)
    

class NoticeboardImage(BaseModel):
    noticeboard = models.ForeignKey(Noticeboard, on_delete=models.CASCADE, related_name='notice_board_image_set')
    image       = models.FileField(upload_to="notice_board",)

# class AdditionalConcept(BaseModel):
#     school      = models.ForeignKey(School, on_delete=models.CASCADE)
#     logomark    = models.ImageField(upload_to="school_additional_concept",blank=True, null=True)
#     title       = models.CharField(max_length=50)
#     image       = models.ImageField(upload_to="school_additional_concept_image", blank=True, null=True)
#     description = models.TextField()









    
    


