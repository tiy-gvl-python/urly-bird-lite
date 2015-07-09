from django.contrib import admin

# Register your models here.
from urlshortner.models import bookmark, click

admin.site.register(bookmark)
admin.site.register(click)