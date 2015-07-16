from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.core.context_processors import csrf
from django.template import RequestContext
from bookmarks.models import Bookmark


def get_index(request):
    context = {}
    context.update(csrf(request))
    return render_to_response('index.html', context)


def redirectOriginal(request, short_id):
    url = get_object_or_404(Bookmark, pk=short_id)
    url.save()
    return HttpResponseRedirect(Bookmark.httpurl)


def user_registration(request):
    if request.POST:
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user_form = UserCreationForm({
            'username': username,
            'password1': password1,
            'password2': password2,
        })
        try:
            user_form.save(commit=True)
            return HttpResponseRedirect("/")
        except ValueError:
            return render_to_response("registration/create_user.html",
                                      {'form': user_form},
                                      context_instance=RequestContext(request))

    return render_to_response("registration/create_user.html",
                              {'form': UserCreationForm()},
                              context_instance=RequestContext(request))


def bookmark_list(request):
    list_of_bookmarks = Bookmark.objects.all().order_by('timestamp')
    context = {"bookmarks": list_of_bookmarks}
    return render_to_response("bookmark_list.html", context, context_instance=RequestContext(request))
