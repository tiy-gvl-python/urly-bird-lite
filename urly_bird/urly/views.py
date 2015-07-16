from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView, DetailView, ListView
from urly.models import Bookmark

from urly.urly_hasher import hasher


class AddUserMixin:
    def form_valid(self, form):
        obj = form.save(commit=False)
        user = self.request.user
        if user.is_authenticated():
            obj.user = user
        return super().form_valid(form)


class HashURLMixin:
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.shorted_url = hasher.encode(obj.url)
        return super().form_valid(form)


class CreateBookmarkView(AddUserMixin, CreateView):
    model = Bookmark
    fields = ["url", "title", "description"]
    template_name = "urly/create_bookmark.html"
    success_url = reverse_lazy("create_bookmark")


def goto_bookmark(request, hash):
    bookmark = Bookmark.objects.filter(shortened_url=hash)
    if bookmark.count() == 1:
        return HttpResponseRedirect(bookmark.get().url)
    return HttpResponseRedirect(reverse_lazy("bookmark_list"))


class BookmarkDetailView(DetailView):
    model = Bookmark
    template_name = "urly/bookmark_detail.html"


class BookmarkListView(ListView):
    model = Bookmark
    template_name = "urly/bookmark_list.html"