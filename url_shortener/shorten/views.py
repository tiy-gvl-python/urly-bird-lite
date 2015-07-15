from django.shortcuts import render
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, RedirectView
from django.http import HttpResponse
# Create your views here.
from .models import Bookmark


#class AllMarks(ListView):
 #   model = Bookmark
  #  fields = []

def home(request):
    return render(request, template_name='home.html')

class AllMarks(ListView):
    model = Bookmark
