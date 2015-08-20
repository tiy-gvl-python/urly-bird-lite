from django.shortcuts import render
from rest_framework import generics
from rest_framework import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from hashids import Hashids
import random
from urlshortner.models import Click, Bookmark
# Create your views here.

class Bookmark_Serializer(serializers.ModelSerializer):


    class Meta:
        model = Bookmark

class Click_Serializer(serializers.ModelSerializer):


    class Meta:
        model = Click


class ViewAllBookmarks(generics.ListAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = Bookmark_Serializer

# Needs User Auth
class UpdateDeleteBookmark(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = Bookmark_Serializer

    def get_queryset(self):
        user = self.request.user
        print(Bookmark.objects.filter(user=user))
        return Bookmark.objects.filter(user=user)

class CreateBookmark(generics.CreateAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = Bookmark_Serializer
    queryset = Bookmark.objects.all()

    def get_queryset(self):
        print(self.request.user)
        return super()

    def post(self, request, *args, **kwargs):
        print("Made it")
        title = self.request.data['title']
        starterurl = self.request.data['starterurl']
        print(starterurl)
        user = self.request.user
        self.request.data['user'] = self.request._auth.user.pk

        hashids = Hashids(salt="generate shoralksdjfsd{}".format(random.random()))
        id = hashids.encode(random.randint(1, 100))
        short = str(id * 1000)[:5]
        self.request.data['shorturl'] = short
        return self.create(request, *args, kwargs={"user": self.request._auth.user.pk , 'title': title, 'shorturl': short})



class ClickStatBookmark(generics.ListAPIView):
    serializer_class = Click_Serializer
    print("YO")

    def get_queryset(self):
        print("Here?")
        return Click.objects.filter(bookmark=Bookmark.objects.get(id=self.kwargs['pk']))


# No way to add foreign Key Yet
class ClickCreateBookmark(generics.CreateAPIView):
    serializer_class = Bookmark_Serializer
    authentication_classes = (TokenAuthentication,)
    queryset = Click.objects.all()
    serializer_class = Click_Serializer

    def post(self, request, *args, **kwargs):
        print("Hey")
        return self.create(request, *args, kwargs={"Bookmark": Bookmark.objects.get(id=self.request.data['Bookmark'])})

#Needs User Auth
class ProfileStats(generics.ListAPIView):
    serializer_class = Bookmark_Serializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Bookmark.objects.filter(user=user)
