from django.db import models
from rest_framework.views import APIView
from django.core.validators import FileExtensionValidator
from portals.base import BaseModel

# Create your models here.

class AboutUs(BaseModel):
    desc = models.TextField(null=True, blank=True)
    videos = models.FileField(upload_to='videos/', validators=[FileExtensionValidator(['mp4', 'avi', 'mov', 'wmv', 'flv'])], null=True, blank=True)

    def save(self,*args, **kwargs):
        count = AboutUs.objects.count()
        print(count)
        if count == 0  :
            return super(AboutUs,self).save(*args, **kwargs)
        else :
            obj = AboutUs.objects.all()
            obj.delete()
            return super(AboutUs,self).save(*args, **kwargs)
        
class Gallery(BaseModel):
    image = models.ImageField(upload_to="img", default=" ", validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])], null=True, blank=True)

    def save(self, *args, **kwargs):
        max_records = 6  
        count = Gallery.objects.count()
        if count < max_records:
            super(Gallery, self).save(*args, **kwargs)
        else:
            oldest_record = Gallery.objects.earliest('id')
            oldest_record.delete()
            super(Gallery, self).save(*args, **kwargs)
