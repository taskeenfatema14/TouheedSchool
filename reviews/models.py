from django.db import models
from schools.models import *
from django.utils import timezone
from portals.base import BaseModel

# Create your models here.

class BoardMember(BaseModel):
    name = models.CharField(max_length=128)
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to='board_members/', null=True, blank=True)

    def _str_(self):
        return f"{self.name} at {self.id}"

class Review(BaseModel):
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    username = models.CharField(max_length=128)
    time = models.TimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    rating = models.IntegerField()
    description = models.TextField()

    def _str_(self):
        return f"Review for {self.school.name} by {self.username}"
