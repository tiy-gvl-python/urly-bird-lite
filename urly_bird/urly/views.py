from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView
from urly.models import Bookmark

from urly.urly_hasher import hasher


class AddUserMixin:
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super().form_valid(form)


class HashURLMixin:
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.shorted_url = hasher.encode(obj.url)
        return super().form_valid(form)


class CreateBookmarkView(AddUserMixin, HashURLMixin, CreateView):
    model = Bookmark
    fields = ["url", "title", "description"]
