from django.shortcuts import render
from rest_framework import generics

# Create your views here.
Viewing, editing, and deleting bookmarks
Seeing the click stats for a bookmark
Adding a click to a bookmark
Allowing a user to see their overall stats (This is a replication of the overall stats page from the original assignment.)



class ViewAllBookmarks(generics)