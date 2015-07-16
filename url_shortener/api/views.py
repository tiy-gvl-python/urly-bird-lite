from django.core.urlresolvers import reverse
from django.shortcuts import render
from rest_framework import serializers, generics
from shorten.models import Bookmark
# Create your views here.


class MySerializer(serializers.ModelSerializer):

    class Meta:
        model = Bookmark


class GetAndPostMarks(generics.ListCreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = MySerializer

class DoesEverythinMarks(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = MySerializer

