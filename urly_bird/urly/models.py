
from django.contrib.auth.models import User
from django.db import models


class Bookmark(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=140)
    url = models.URLField()
    shortened_url = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now=True)


class Click(models.Model):
    user = models.ForeignKey(User)
    bookmark = models.ForeignKey(Bookmark)
    created = models.DateTimeField(auto_now=True)
