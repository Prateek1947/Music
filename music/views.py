from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Album, Song
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.views import generic

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    template_name = 'music/details.html'
    model = Album

    def get_queryset(self):
        return super().get_queryset()


class CreateAlbum(generic.CreateView):
    model = Album
    fields = ['artist', 'album_title', 'genre', 'album_logo']


# def index(request):
#     albums = Album.objects.all()
#     template = loader.get_template('music/index.html')
#     context = {
#         'albums': albums
#     }
#     return HttpResponse(template.render(context, request))


# def details(request, album_id):
#     albums = Album.objects.all()
#     try:
#         album = albums.get(id=album_id)
#     except Album.DoesNotExist:
#         raise Http404('Album Does Not Exists')
#     return render(request, 'music/details.html', {'songs': album.song_set.all(), 'album': album})


# def favourite(request, album_id):
#     album = get_object_or_404(Album, id=album_id)
#     try:
#         selected_song = album.song_set.get(id=request.POST['song'])
#     except (KeyError, Song.DoesNotExist):
#         return render(request, 'music/details.html', {'songs': album.song_set.all(), 'album': album, 'error_message': "You have not selected any item"})
#     else:
#         selected_song.is_favourite = True
#         selected_song.save()
#         return render(request, 'music/details.html', {'songs': album.song_set.all(), 'album': album})
