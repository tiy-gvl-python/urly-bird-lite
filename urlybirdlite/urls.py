"""urlybirdlite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url

from django.views.generic import RedirectView
from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from urlshortner.models import Bookmark
from urlshortner.views import home, CreateBookMark, BookmarkUpdate, BookmarkDelete, profile, wtd, wtupdate, redirec, \
    ouser, allbookmarks

urlpatterns = [

    url(r'^api/', include('url_api.urls')),

    url('^register/', CreateView.as_view(
            template_name='registration/create_user.html',
            form_class=UserCreationForm,
            success_url='/profile/'), name="regis"),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/$', 'django.contrib.auth.views.login',name="login"),
    url(r'^logout', 'django.contrib.auth.views.logout', name="logout"),

    url('^Bookmark/', CreateBookMark.as_view(
        template_name='createbookmark.html',
        success_url='/profile/'), name="createbookmark"),

    url(r'^wtd/', wtd, name="wtd"),
    url(r'^uwtupdate/', wtupdate, name="wtupdate"),

    url(r'^profile/', profile, name="profile"),

    url('^delrate(?P<pk>\w+)', BookmarkDelete.as_view(
        template_name='deletebookmark.html',
        success_url='/profile/'), name="delbookmark"),

    url('^update(?P<pk>\w+)', BookmarkUpdate.as_view(
        template_name='bookmark_update.html',
        success_url='/profile/'), name="updatebookmark"),

    url(r'^7(?P<shorturl>\w+)/$', redirec),
    #url(r'^7(?P<shorturl>\w+)/$', RedirectView.as_view(url="shorturl")),
    url(r'^user(?P<id>\d+)/$', ouser),
    url(r'^all/$', allbookmarks, name="all"),


    #(r'^7(?P<shorturl>\w+)/$', RedirectView.as_view()),


    ]