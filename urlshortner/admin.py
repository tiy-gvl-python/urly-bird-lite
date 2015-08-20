from django.contrib import admin
import rest_framework
from rest_framework.authentication import Token

# Register your models here.
from urlshortner.models import Bookmark, Click



admin.site.register(Bookmark)
admin.site.register(Click)
