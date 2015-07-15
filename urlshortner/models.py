import hashids
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models import Model


class BookmarkManager(models.Manager):
    pass


class Bookmark(models.Model):
    user = models.ForeignKey(User)
    starterurl = models.CharField(max_length=250)
    shorturl = models.CharField(max_length=45)
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=140, blank=True)
    created = models.DateTimeField(auto_now=True)

    objects = BookmarkManager()

    def __str__(self):
        return "{} - {} - {} - {} - {} - {}".format(self.user, self.starterurl, self.shorturl, self.title, self.description, self.id)

    class Meta:
        ordering = ['-created']

class Click(models.Model):
    bookmark = models.ForeignKey(Bookmark)
    used = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} - {}".format(self.used, self.id)