from django.db import models
from django.core.urlresolvers import reverse

class Bookmark(models.Model):
    hashed = models.CharField(max_length=8)
    description = models.CharField(max_length=150)
    url = models.URLField()
    title = models.CharField(max_length=150)


class Click(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    bookmark = models.ForeignKey(Bookmark)



    def __str__(self):
        return"{}-{}-{}".format(self.user, self.bookmark)
