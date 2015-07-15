from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Bookmark(models.Model):
    user = models.ForeignKey(User)
    code = models.CharField(max_length=50)
    title = models.CharField(max_length=20, null=True)
    link = models.CharField(max_length=250)
    date = models.DateField(auto_now_add=True)



    def __str__(self):
        return "User: {}, Title {}, Date: {}".format(self.pk,
                                                     self.title,
                                                     self.date)


class Click(models.Model):
    who = models.ForeignKey(User)
    bookmark = models.OneToOneField(Bookmark)
    time = models.DateField(auto_now_add=True)

    def __str__(self):
        return 'Who: {}, Bookmark: {}, Time: {}'.format(self.who.pk,
                                                        self.bookmark,
                                                        self.time)

