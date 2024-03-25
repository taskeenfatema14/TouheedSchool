from django.db import models
import uuid
# from rest_framework.views import APIView

# Create your models here.


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True,editable=False)
    updated_on = models.DateTimeField(auto_now=True)
 
    class Meta:
        abstract = True
        ordering = ("-created_on",)
