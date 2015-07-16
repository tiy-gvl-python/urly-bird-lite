from django.contrib.auth.models import User
from django.db import models

# Create your models here.



class Profile(models.Model):
    user = models.OneToOneField(User)
    key = models.CharField(max_length=60, blank=True)

