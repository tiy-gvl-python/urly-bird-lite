from django.contrib.auth.models import User
from django.db import models
from hashids import Hashids

# Create your models here.

class Bookmark(models.Model):
    user = models.ForeignKey(User, null=True)
    title = models.CharField(max_length=20, null=True)
    link = models.CharField(max_length=250)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "User: {}, Title {}, Date: {}".format(self.pk,
                                                     self.title,
                                                     self.date)

    def code(self):
        secret = Hashids(salt='I love Bananas 26')
        number = secret.encode(self.pk)
        return number


class Click(models.Model):
    who = models.ForeignKey(User)
    bookmark = models.OneToOneField(Bookmark)
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'Who: {}, Bookmark: {}, Time: {}'.format(self.who.pk,
                                                        self.bookmark,
                                                        self.time)

