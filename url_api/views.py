from django.shortcuts import render
from rest_framework import generics
from rest_framework import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from urlshortner.models import Click, Bookmark
# Create your views here.

class Bookmark_Serializer(serializers.ModelSerializer):
    print("hey")

    #def create(self, validated_data):
     #   user =

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
        title = self.request.data['title']
        starterurl = self.request.data['starterurl']

        print("Hey")
        return self.create(request, *args, kwargs={"user": self.request.user,'title': title,  })



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
        return self.create(request, *args, kwargs={"bookmark": Bookmark.objects.get(id=self.request.data['bookmark'])})

#Needs User Auth
class ProfileStats(generics.ListAPIView):
    serializer_class = Bookmark_Serializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        user = self.request.user
        return Bookmark.objects.filter(user=user)
