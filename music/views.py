from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Album, Song
from django.template import loader
from django.shortcuts import render, get_object_or_404

# Create your views here.


def index(request):
    albums = Album.objects.all()
    template = loader.get_template('music/index.htm')
    context = {
        'albums': albums
    }
    return HttpResponse(template.render(context, request))


def details(request, album_id):
    albums = Album.objects.all()
    try:
        album = albums.get(id=album_id)
    except Album.DoesNotExist:
        raise Http404('Album Does Not Exists')
    return render(request, 'music/details.html', {'songs': album.song_set.all(), 'album': album})


def favourite(request, album_id):
    album = get_object_or_404(Album, id=album_id)
    try:
        selected_song = album.song_set.get(id=request.POST['song'])
    except (KeyError, Song.DoesNotExist):
        return render(request, 'music/details.html', {'songs': album.song_set.all(), 'album': album, 'error_message': "You have not selected any item"})
    else:
        selected_song.is_favourite = True
        selected_song.save()
        return render(request, 'music/details.html', {'songs': album.song_set.all(), 'album': album})
