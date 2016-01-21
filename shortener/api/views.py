import random
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.http import request
from django.shortcuts import render
from hashids import Hashids
from rest_framework import generics, serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated


from subjectivity.models import Bookmark, Clicker

class BookmarkSerializer(serializers.ModelSerializer):
    #  earl = serializers.SerializerMethodField()

    #  def get_earl(self, obj):
        #  return reverse('all_things', kwargs={"pk": obj.pk})

    class Meta:
        model = Bookmark


class ClickerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Clicker


class BookmarkListAPIView(generics.ListAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer


class BookmarkAllAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookmarkSerializer
    permission_classes = (IsAuthenticated, )
    authentication_classes = (TokenAuthentication,)

    def get_queryset(self):
        return Bookmark.objects.filter(user=self.request.user)


class BookmarkListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = BookmarkSerializer
    #permission_classes = (IsAuthenticated, )
    #authentication_classes = (TokenAuthentication, )
    fields = ["title", "description", "url"]
    queryset = Bookmark.objects.all()
    #def get_queryset(self):
     #   return Bookmark.objects.filter(user=self.request.user)


class ClickerListAPIView(generics.ListAPIView):
    queryset = Clicker.objects.all()
    serializer_class = ClickerSerializer


class ClickerAllAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Clicker.objects.all()
    serializer_class = ClickerSerializer


