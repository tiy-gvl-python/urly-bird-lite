from django.contrib import admin

# Register your models here.
from urly.models import Bookmark, Click

admin.site.register(Bookmark)
admin.site.register(Click)