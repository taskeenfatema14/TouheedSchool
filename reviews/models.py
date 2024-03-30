from django.db import models
from schools.models import *
from django.utils import timezone
from portals.base import BaseModel

# Create your models here.
class BoardMember(BaseModel):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='board_members/', null=True, blank=True)

    def _str_(self):
        return f"{self.name} at {self.id}"

class Review(BaseModel):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    time = models.TimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    rating = models.IntegerField()

    def _str_(self):
        return f"Review for {self.school.name} by {self.username}"
    

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