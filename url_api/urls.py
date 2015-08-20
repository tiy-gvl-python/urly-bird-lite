from django.conf.urls import include, url


from urlshortner.models import Bookmark
from url_api.views import  ViewAllBookmarks, UpdateDeleteBookmark, ClickStatBookmark, ClickCreateBookmark, ProfileStats, CreateBookmark

urlpatterns = [

    url(r'^bookmarks/$', ViewAllBookmarks.as_view(), name="view_bookmarks"),
    url(r'^create/$', CreateBookmark.as_view(), name="create_bookmarks"),
    url(r'^updatedelete/(?P<pk>\d+)/$', UpdateDeleteBookmark.as_view(), name="updatedelete_bookmarks"),
    url(r'^click/(?P<pk>\d+)/$', ClickStatBookmark.as_view(), name="clicks_bookmarks"),
    url(r'^clickcreate/$', ClickCreateBookmark.as_view(), name="clickscreate_bookmarks"),
    url(r'^profilestats/$', ProfileStats.as_view(), name="profile_bookmarks"),




    ]