from django.db import models
from django.contrib.auth.models import AbstractUser
import os


class ExtraUser(AbstractUser):
    """Extra User Model"""
    pass


class AudioFileModel(models.Model):
    """AudioFile model. Keeps audio files and description"""
    audio_file = models.FileField(upload_to="file_storage/", verbose_name='Audio files', )
    description = models.CharField(max_length=50, verbose_name="Audio File description")

    def __str__(self):
        return self.description if len(str(self.description)) < 20 \
            else self.description[:20] + "..."

    def filename(self):
        """method returns file name"""
        return os.path.basename(self.audio_file.name)

    class Meta:
        verbose_name = "Audio File"
        verbose_name_plural = "Audio Files"

