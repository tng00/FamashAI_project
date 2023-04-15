from django.db import models


class UserImage(models.Model):
    image = models.ImageField(upload_to='images')
    obj_file = models.FileField(upload_to='obj_files', null=True, blank=True)
    Flame_file = models.FileField(upload_to='Flame_files', null=True, blank=True)