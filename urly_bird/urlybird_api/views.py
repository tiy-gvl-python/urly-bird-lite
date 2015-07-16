from django.shortcuts import render
from rest_framework import generics
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from bookmarks.models import Bookmark, Click
from rest_framework import serializers
from hashids import Hashids
import random


class BirdSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookmark

class ClickSerializer(serializers.ModelSerializer):

    class Meta:
        model = Click



class ListUrl(generics.ListAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BirdSerializer

# I am structuring everything similar to how bekk did his.
# I feel like I have a decent understanding of API's but not shortening the urls.

class DeleteUpdateRetrieveUrl(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BirdSerializer
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        user = self.request.user
        return Bookmark.objects.filter(user=user)



class CreateUrl(generics.CreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BirdSerializer
    permission_classes = (IsAuthenticated,)
    authentication_class = (TokenAuthentication,)

    def get_queryset(self):
        return super()


#I don't really understand this function.

    def post(self, request, *args, **kwargs):
        title = self.request.data['title']
        originalurl = self.request.data['url']
        user = self.request.user
        self.request.data['user'] = self.request._auth.user.pk

        hash_url = Hashids(salt="this is the salt{}".format(random.random()))
        url_id = hash_url.encode(random.randint(1, 50))
        short_url = str(url_id * 100)[:5]
        self.request.date['hashed'] = short_url
        return self.create(request, *args, kwargs={'user': self.request.user, 'title': title, })


class ClickStatList(generics.ListAPIView):
    serializer_class = ClickSerializer

    def get_queryset(self):
        #                                                     I don't understand what this is below.
        return Click.objects.filter(bookmark=Bookmark.objects.get(id=self.kwargs['pk']))
