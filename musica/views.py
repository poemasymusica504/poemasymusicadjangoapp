from django.shortcuts import render, redirect, get_object_or_404
from .forms import MusicForm
from .models import Music
# Create your views here.


def crear_song(request):

    if request.method == 'GET':
        return render(request, 'crear_song.html', {
            'form': MusicForm
        })
    else:
        try:
            form = MusicForm(request.POST, files=request.FILES)
            new_song = form.save(commit=False)
            new_song.user = request.user
            new_song.save()
            return redirect('canciones_app:songs')
        except ValueError:
            return render(request, 'crear_song.html', {
            'form': MusicForm,
            'error': 'Please provide valide data'
        })

def music(request):
    music_list = Music.objects.all().order_by('-fecha')

    return render(request, "musica.html", {
        "music_list": music_list
    })
