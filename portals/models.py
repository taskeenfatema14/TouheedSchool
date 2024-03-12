from django.db import models

# Create your models here.


class BaseModel(models.Model):
    id         = models.AutoField(primary_key=True,editable=False)
    created_on = models.DateTimeField(auto_now_add=True,editable=False)
    updated_on = models.DateTimeField(auto_now=True)
 
    class Meta:
        abstract = True
        ordering = ("-created_on",)
