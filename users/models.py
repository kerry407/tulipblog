from django.db import models
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe
from PIL import Image
from django.dispatch import receiver
from django.shortcuts import reverse
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250, default='None')
    last_name = models.CharField(max_length=250, default='None')
    bio = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=40,null=True, blank=True)
    profile_image = models.ImageField(default='images/default.png', upload_to = 'images')
    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.user.username} Profile'


    def save(self):
        super().save()

        img = Image.open(self.profile_image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.profile_image.path)





