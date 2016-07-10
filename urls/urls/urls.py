from django.contrib import admin
from django.conf.urls import include, url
from django.contrib.auth.views import login, logout
from urls_app.views import base, user_registration, CreateBookMark, encode

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', base, name='base'),
    url(r'^accounts/login/', login, name='login'),
    url(r'^logout/', logout, name='logout'),
    url(r'^registration/', user_registration, name='user_registration'),
    url(r'^bookmark/', CreateBookMark.as_view(temp), name='create_bookmark'),
    url(r'^search/(?P<word>\w+)/', encode),
]
