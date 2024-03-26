from django.db import models
from schools.models import *
from django.utils import timezone

# Create your models here.
class BoardMember(models.Model):
    board_id = models.AutoField(primary_key=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='board_members/', null=True, blank=True)

    def _str_(self):
        return self.name

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    time = models.TimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    rating = models.IntegerField()

    def _str_(self):
        return f"Review for {self.school.name} by {self.username}"