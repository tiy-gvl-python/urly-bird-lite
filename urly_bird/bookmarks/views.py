from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.template import RequestContext
from bookmarks.models import Click


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
    list_of_bookmarks = Click.objects.all().order_by('timestamp')
    context = {"bookmarks": list_of_bookmarks}
    return render_to_response("bookmark_list.html", context, context_instance=RequestContext(request))


