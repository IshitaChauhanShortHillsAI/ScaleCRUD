# Create your models here.
from django.db import models

class Artist(models.Model):
    ArtistId = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
