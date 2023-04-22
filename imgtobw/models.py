from django.db import models


class UploadImage(models.Model):
    image = models.ImageField(upload_to='images')
