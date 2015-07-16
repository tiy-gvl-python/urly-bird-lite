__author__ = 'pnitto'

from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from .views import ListUrl, DeleteUpdateRetrieveUrl, CreateUrl, ClickStatList


urlpatterns = [
    url(r'^bird/$',ListUrl.as_view(), name="list_bookmarks"),
    url(r'^deleteupdate/(?P<pk>\d+)/$', DeleteUpdateRetrieveUrl.as_view(), name="deleteupdate"),
    url(r'^create/$', CreateUrl.as_view(), name="create"),
    url(r'^statlist/(?P<pk>\d+)/$', ClickStatList.as_view(), name="statlist")


    ]