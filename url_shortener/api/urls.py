from django.conf.urls import include, url
from .views import GetAndPostMarks, DoesEverythinMarks


urlpatterns =[

    url(r'^bookmarks/$', GetAndPostMarks.as_view(), name='get_post_create_api'),
    url(r'^bookmarks/(?P<pk>\d+)$',
        DoesEverythinMarks.as_view(),
        name='put_update_delete_api'),

]