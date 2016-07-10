from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver


class Bookmark(models.Model):
    user = models.ForeignKey(User, null=True)
    url = models.URLField(max_length=120)
    hash = models.CharField(max_length=64)
    title = models.CharField(max_length=15)
    description = models.CharField(max_length=300)

    @receiver(pre_save)
    def update_hash(sender=Bookmark, instance, *args, **kwargs):
        instance.hash = "Hey" #models.b32encode(instance.user + instance.url + instance.title)


class Click(models.Model):
    user = models.ForeignKey(User, null=True)
    bookmark = models.ForeignKey(Bookmark)
    timestamp = models.DateField(auto_now=True)