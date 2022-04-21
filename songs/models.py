from django.db import models

# Create your models here.
class Song(models.Model):
    artist = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    class Meta:
      verbose_name_plural = "songs"

    def __str__(self):
        return self.title