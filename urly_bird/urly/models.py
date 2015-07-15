
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from urly.urly_hasher import hasher


class Bookmark(models.Model):
    user = models.ForeignKey(User, null=True)
    title = models.CharField(max_length=25)
    description = models.CharField(max_length=140)
    url = models.URLField()
    shortened_url = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)


class Click(models.Model):
    user = models.ForeignKey(User, null=True)
    bookmark = models.ForeignKey(Bookmark)
    created = models.DateTimeField(auto_now_add=True)


@receiver(post_save, sender=Bookmark)
def create_shortened_url(sender, instance, **kwargs):
    if not instance.shortened_url:
        instance.shortened_url = hasher.encode(instance.id)
        instance.save()
