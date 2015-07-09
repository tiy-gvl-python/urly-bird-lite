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
from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.contrib.auth.views import login, logout
from bookmarks.views import bookmark_list, user_registration, get_index, redirectOriginal

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/', login, name="login"),
    url(r'^logout/', logout, {'next_page':'/'}, name="logout"),
    url(r'^$', bookmark_list, name="bookmark_list"),
    url(r'^registration/', user_registration, name="user_registration"),
    url(r'^get_index/', get_index, name='get_index'),
    url(r'^redirectOriginal/(?P<short_id>\d+)/$', redirectOriginal, name="redirectOriginal")
    #url(r'',include('bookmarks.urls', namespace='bookmarks')),

]
