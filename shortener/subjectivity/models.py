from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Bookmark(models.Model):
    title = models.CharField(max_length=30)
    url = models.URLField()
    description = models.CharField(max_length=140, blank=True)
    user = models.ForeignKey(User, null=True)
    hashed = models.CharField(max_length=10, null=True)

    def __str__(self):
        return self.title

#  class Booker(models.Model):
#    user = models.OneToOneField(User)

#class Hashed(models.Model):
#    hashid = CharField(max_length=8)
#bookmark = models.OneToOneField(Bookmark)
