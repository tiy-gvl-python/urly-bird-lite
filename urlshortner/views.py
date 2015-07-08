from django.shortcuts import render, render_to_response

# Create your views here.

def home(requests):
    context={}
    return render_to_response("home.html", context)
