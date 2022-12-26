from django.db import models


# Create your models here.
class CountVehicles(models.Model):
    video = models.FileField(upload_to='videos/', max_length=255, blank=True)
    video_output = models.FileField(upload_to='output/', max_length=255, blank=True)