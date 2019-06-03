from django.db import models
from django.contrib.auth.models import AbstractUser


class ExtraUser(AbstractUser):
    """Extra User Model"""
    pass


class AudioFileModel(models.Model):
    audio_file = models.FileField
