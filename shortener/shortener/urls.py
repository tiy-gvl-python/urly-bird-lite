"""shortener URL Configuration

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
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import login, logout
from django.views.generic.edit import CreateView

from subjectivity import views

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'api/', include('api.urls')),
    url(r'^registration/$', views.Registration.as_view(), name="registration"),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^bookmarks/$', views. , name="bookmarks"),
    url(r'^users/$', views.UserList.as_view(), name="users"),
    url(r'^user_detail/(?P<pk>\d+)/', views.UserDetailView.as_view(), name="user_detail"),
    url(r'^accounts/login/', login, name="login"),
    url(r'^logout/', logout, {'next_page': '/'}, name="logout"),
    url(r'^mark/$', views.CreateBookMark.as_view(success_url='/'), name="marked"),
    url(r'mark_list/$', views.BookmarkList.as_view(), name='mark_list'),
    url(r'mark_list/(?P<pk>\d+)/', views.BookmarkDetail.as_view(), name='mark_detail'),
    url(r'^(?P<hashed>\w+)/$', views.url_redirect, name='redirect'),
]
