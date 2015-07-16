from django.db import models

# Create your models here.

class ShortenUrls(models.Model):
    short_url = models.CharField(max_length=50)
    long_url = models.CharField(max_length=300)
    description = models.CharField(max_length=50)