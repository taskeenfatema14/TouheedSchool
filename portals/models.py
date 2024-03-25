from django.db import models

# Create your models here.


class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True,editable=False, null = True, blank = True)
    updated_on = models.DateTimeField(auto_now=True)
 
    class Meta:
        abstract = True
        ordering = ("-created_on",)

