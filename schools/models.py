from django.db import models
from django.utils import timezone

class School(models.Model):
    school_id = models.CharField(max_length=20, primary_key=True)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='school_images/', null=True, blank=True)
    video = models.FileField(upload_to='school_videos/', null=True, blank=True)
    location = models.CharField(max_length=200)
    courses = models.TextField()
    facility = models.TextField()
    description = models.TextField()
    principal = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class BoardMember(models.Model):
    board_id = models.AutoField(primary_key=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='board_members/', null=True, blank=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    username = models.CharField(max_length=100)
    time = models.TimeField(default=timezone.now)
    date = models.DateField(default=timezone.now)
    rating = models.IntegerField()

    def __str__(self):
        return f"Review for {self.school.name} by {self.username}"
