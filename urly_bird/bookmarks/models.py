from django.db import models
from django.core.urlresolvers import reverse

class User(models.Model):
    title_bookmark = models.CharField(max_length=50)
    url_description = models.CharField(max_length=100)



class Click(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    short_id = models.SlugField(max_length=8, primary_key=True)
    http_url = models.URLField(max_length=200)

    def reverse_order(self):
        order = reverse('timestamp')



    def __str__(self):
        return"{}-{}-{}".format(self.user, self.bookmark, self.timestamp)
