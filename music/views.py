from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("<h1>Hey there, welcome to my first django webapp</h1>")


def details(request, album_id):
    return HttpResponse("   "+album_id)