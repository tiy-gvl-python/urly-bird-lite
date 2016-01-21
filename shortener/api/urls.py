from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^$', views.BookmarkListAPIView.as_view(), name='bookmark_list'),
    url(r'^bookmarks/$', views.BookmarkListAPIView.as_view(), name='bookmark_list'),
    url(r'bookmarks/(?P<pk>\d+)/', views.BookmarkAllAPIView.as_view(), name='bookmark_all'),
    url(r'bookmarker/$', views.BookmarkListCreateAPIView.as_view(), name='bookmark_create'),
    url(r'clicks/$', views.ClickerListAPIView.as_view(), name='clicks'),
    url(r'clicks/(?P<pk>\d+)/', views.ClickerAllAPIView.as_view(), name='clicker'),
]

#(?P<pk>\d+)/