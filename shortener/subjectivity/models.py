import random
from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from hashids import Hashids

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class Bookmark(models.Model):
    title = models.CharField(max_length=30)
    url = models.URLField()
    description = models.CharField(max_length=140, blank=True)
    user = models.ForeignKey(User, null=True)
    hashed = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.title


class Clicker(models.Model):
    bookmark = models.ForeignKey(Bookmark)
    time = models.DateTimeField(auto_now_add=True)


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     for user in User.objects.all():
#         Token.objects.get_or_create(user=user)
#     if created:
#         Token.objects.create(user=instance)


@receiver(post_save, sender=Bookmark)
def create_hashed(sender, instance, **kwargs):
    if not instance.hashed:
        hashids = Hashids(salt=str([random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randint(10,30))]))
        hashid = hashids.encode(str([random.randint(1, 10) for i in range(random.randint(3, 10))]))
        rehash = Hashids(salt=str(hashid), min_length=7)
        instance.hashed = rehash.encode(5)
        instance.save()

