from django.shortcuts import render
from django.views.generic import ListView, CreateView, \
    DeleteView, UpdateView, RedirectView, DetailView

from django.http import HttpResponse
# Create your views here.
from .models import Bookmark, Click



def home(request):
    return render(request, template_name='home.html')

class AllMarks(ListView):
    model = Bookmark


class SingleMark(DetailView):
    model = Bookmark


class DeleteMark(DeleteView):
    model = Bookmark
    template_name = 'shorten/bookmark_detail.html'


