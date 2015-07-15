from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Bookmark(models.Model):
    user = models.ForeignKey(User)
    url = models.URLField()
    shortened_url = models.CharField(max_length=50)
    created = models.TimeField(auto_now=True)


class History(models.Model):
    user = models.ForeignKey(User)
    bookmark = models.ForeignKey(Bookmark)
    created = models.TimeField(auto_now=True)
