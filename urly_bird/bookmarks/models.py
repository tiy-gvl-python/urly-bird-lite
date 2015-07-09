from django.db import models

class User(models.Model):
    url_title = models.CharField(max_length=50)
    url_description = models.CharField(max_length=100)



class Click(models.Model):
    user = models.ForeignKey(User)
    timestamp = models.DateTimeField(auto_now_add=True)
    short_id = models.SlugField(max_length=8, primary_key=True)
    http_url = models.URLField(max_length=200)




    def __str__(self):
        return"{}-{}-{}".format(self.user, self.bookmark, self.timestamp)
