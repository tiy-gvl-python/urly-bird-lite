"""urly_bird URL Configuration

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
from django.contrib import admin
from urly import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^bookmark/create/$', views.CreateBookmarkView.as_view(), name="create_bookmark"),
    url(r'^b/(?P<hash>\w+)/$', views.goto_bookmark, name="goto_bookmark"),
    url(r'^bookmark/(?P<pk>\d+)/$', views.BookmarkDetailView.as_view(), name="bookmark_detail"),
    url(r'^bookmark/$', views.BookmarkListView.as_view(), name="bookmark_list"),
]
