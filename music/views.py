from django.shortcuts import render
from django.http import HttpResponse
from .models import Album

# Create your views here.


def index(request):
    html=''
    albums=Album.objects.all()
    for album in albums:
        url='/music/'+str(album.id)+'/'
        html+='<a href="'+url+'"> '+album.album_title+'</a><br>'
    return HttpResponse(html)


def details(request, album_id):
    return HttpResponse(album_id)