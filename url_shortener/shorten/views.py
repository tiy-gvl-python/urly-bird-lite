from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.views.generic import ListView, CreateView, \
    DeleteView, UpdateView, RedirectView, DetailView
from rest_framework.authtoken.models import Token

from django.http import HttpResponse
# Create your views here.
from api.models import Profile
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


def token_create(request):
    token = Token.objects.create(user=request.user)
    request.key = token.key
    request.save()

@login_required
def activate_work(request):
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    keyword = 'hello world'
    print(user)
    print(request.POST['code'])
    token = Token.objects.create(user=user)
    context = {}
    print('I am at the input')
    if request.POST:
        print('hey I dont work')
        x = request.POST['code']
        print(x)
        print('I am at the first if statement')
        profile = Profile.objects.get(user=user)
        if x == keyword:
            profile.key = token.key
            profile.save()
            print('tokenized')
            return redirect('shorten:key')
        else:
            redirect('shorten:denied')
        profile.save()
        context['profile'] = profile
    return render_to_response("registration/add_permissions.html", context_instance=RequestContext(request))


@login_required
def activate(request):
    return render_to_response("registration/add_permissions.html", context_instance=RequestContext(request))



def permission_denied(requests):
    return render_to_response("shorten/denied.html",
                              context_instance=RequestContext(requests))