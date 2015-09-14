from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.utils.decorators import method_decorator
from django.views import generic
from django.views.generic import ListView, DetailView, UpdateView
from django.shortcuts import render_to_response as rtr
from django.template import RequestContext
from django.views.generic.edit import CreateView


from .models import Bookmark, Clicker, User
from hashids import Hashids
import random


class LoginRequiredMixin(object):
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


def home(request):
    context = {}
    return rtr("home.html", context, context_instance=RequestContext(request))


class Registration(generic.FormView):
    template_name = 'registration/create_user.html'
    form_class = UserCreationForm
    success_url = '/'

    #  auto-login
    def form_valid(self, form):
      form.save()
      username = self.request.POST['username']
      password = self.request.POST['password1']
      user = authenticate(username=username, password=password)
      login(self.request, user)
      Bookmark.objects.create(user=user)
      return super().form_valid(form)


class BookmarkList(LoginRequiredMixin, ListView):
    model = Bookmark
    template_name = 'bookmark_list.html'

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)


class BookmarkDetail(LoginRequiredMixin, DetailView):
    model = Bookmark
    template_name = 'bookmark_detail.html'
    fields = ["title", "url", "description", "hashed", "user"]


class UserList(LoginRequiredMixin, ListView):
    model = User
    template_name = 'user_list.html'


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user_detail.html'


def url_redirect(request, hashed):
    bookmark = Bookmark.objects.get(hashed=hashed)
    url = bookmark.url
    Clicker.objects.create(bookmark=bookmark)
    return redirect(url)

class CreateBookMark(LoginRequiredMixin, CreateView):  # Some more Bekk Magic
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
        return super().form_valid(form)


