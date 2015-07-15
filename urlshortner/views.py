from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
import random
# Create your views here.
from django.views.generic import CreateView, DeleteView, UpdateView, RedirectView
from hashids import Hashids
from urlshortner.models import bookmark, click
from django.shortcuts import redirect



def redirec(requests, shorturl):
    print(shorturl)
    url = bookmark.objects.get(shorturl=shorturl)
    time = click.objects.create(bookmark=url)
    time.save()
    url = url.starterurl
    print(url)
    context = {"ur":url}
    return render_to_response("redirec.html", context)

def ouser(requests, id):
    profile_book = bookmark.objects.filter(user=User.objects.get(id=id))
    context = {'userbookmark': profile_book}
    return render_to_response("userbookmark.html", context)

def allbookmarks(requests):
    profile_book = bookmark.objects.all()
    context = {'userbookmark': profile_book}
    return render_to_response("allbookmarks.html", context)

def home(requests):
    context = {}
    return render_to_response("home.html", context)


def profile(requests):
    profile_book = bookmark.objects.filter(user=User.objects.get(id = requests.user.id))
    context = {'bookmarks': profile_book}
    return render_to_response("profile.html", context)


def wtd(requests):
    delete_book = bookmark.objects.filter(user=requests.user)
    context = {'bookmarks': delete_book}
    return render_to_response("wtd.html", context)


def wtupdate(requests):
    update_book = bookmark.objects.filter(user=requests.user)
    context = {'bookmarks': update_book}
    return render_to_response("wtupdate.html", context)


class CreateBookMark(CreateView):
    model = bookmark
    print("Ran past model")
    template_name = "createbookmark.html"
    print("Ran past template")
    success_url = ""
    print("Ran past success url")
    fields = ["starterurl", "title", "description"]
    print("Ran past fields")

    def form_valid(self, form):
        hashids = Hashids(salt="generate shoralksdjfsd{}".format(random.random()))
        id = hashids.encode(random.randint(1, 100))
        print("StarterUrl", form.instance.starterurl)
        print("id", id)
        print("Test")
        print("User", self.request.user)
        form.instance.user = self.request.user
        print("shorturl", id)
        short = str(id * 1000)[:5]
        print(short)
        form.instance.shorturl = short
        return super().form_valid(form)


class BookmarkDelete(DeleteView):
    model = bookmark
    success_url = reverse_lazy('profile')


class BookmarkUpdate(UpdateView):
    model = bookmark
    fields = ['title', 'description']
    template_name = 'bookmark_update.html'
