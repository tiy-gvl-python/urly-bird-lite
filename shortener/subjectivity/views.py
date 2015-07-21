from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.shortcuts import render_to_response as rtr
from django.template import RequestContext
from django.views.generic.edit import CreateView


from .models import Bookmark, Clicker, User
from hashids import Hashids
import random


def hasher(n):
    hashid = hashids.encode(str([random.randint(1, 10) for i in range(random.randint(3, 10))]))
    rehash = Hashids(salt=str(hashid), min_length=7)
    rehashid = rehash.encode(n)
    return rehashid


def home(request):
    context = {}
    return rtr("base.html", context, context_instance=RequestContext(request))


class BookmarkList(ListView):
    model = Bookmark
    template_name = 'bookmark_list.html'


class BookmarkDetail(DetailView):
    model = Bookmark
    template_name = 'bookmark_detail.html'
    fields = ["title", "url", "description", "hashed", "user"]


class UserList(ListView):
    model = User
    template_name = 'user_list.html'


def url_redirect(request, hashed):
    bookmark = Bookmark.objects.get(hashed=hashed)
    url = bookmark.url
    click = Clicker.objects.create(bookmark=bookmark)
    #context = {"url": url}
    #return rtr('redirect.html', context, context_instance=RequestContext(request))
    return redirect(url)

class CreateBookMark(CreateView):  # Some more Bekk Magic
    model = Bookmark
    template_name = "create_bookmark.html"
    success_url = ""
    fields = ["title", "url", "description"]

    def form_valid(self, form):
        user = self.request.user
        hashids = Hashids(salt=str([random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(random.randint(10,30))]))
        hashid = hashids.encode(str([random.randint(1, 10) for i in range(random.randint(3, 10))]))
        rehash = Hashids(salt=str(hashid), min_length=7)
        rehashid = rehash.encode(user.id)
        form.instance.user = user
        form.instance.hashed = rehashid
        return super().form_valid(form)  # Causality has been denied


