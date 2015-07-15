
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.views.generic import ListView
from django.shortcuts import render_to_response as rtr
from django.template import RequestContext
from django.views.generic.edit import CreateView


from .models import Bookmark, User
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


class UserList(ListView):
    model = User
    template_name = 'user_list.html'


def url_changer(request, bookmark_id):
    bookmark = Bookmark.objects.get(id=bookmark_id)
    user = User.objects.get(bookmark__pk=bookmark_id).pk
    hashed = hasher(user)
    Hashed.objects.create(hashid=hashed, bookmark=bookmark)
    all_hash = Hashed.objects.all
    context = {"hash": hashed}
    return rtr()


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

def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
        muser = Movie.objects.filter(rating__user=user)
    except User.DoesNotExist:
        return HttpResponseNotFound("NOT FOUND!")
    context = {"user": user, "muser": muser}
