# from django.db import models
# import uuid


# # Create your models here.

# class BaseModel(models.Model):
#     id         = models.UUIDField(default=uuid.uuid4,primary_key=True)
#     created_on = models.DateTimeField(auto_now_add=True,editable=False)
#     updated_on = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True
#         ordering = ("-created_on",)


<<<<<<< HEAD
=======
class BaseModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True,editable=False, null = True, blank = True)
    updated_on = models.DateTimeField(auto_now=True)
 
    class Meta:
        abstract = True
        ordering = ("-created_on",)

>>>>>>> 749970f3ea87b628f1a409a0234452924fd0221f
