from django.db import models

# Create your models here.
class FileUpload(models.Model):
    jsonFile = models.FileField(null=True, blank=False)