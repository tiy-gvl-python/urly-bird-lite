from django.conf.urls import include, url


from urlshortner.models import bookmark
from urlshortner.views import home

urlpatterns = [

    url(r'^api/', include('url_api.urls')),

    ]