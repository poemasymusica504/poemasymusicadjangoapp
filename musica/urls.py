from django.contrib import admin
from django.urls import path
from . import views

app_name = 'canciones_app'

urlpatterns = [
    path(
        'crear/cancion',
        views.crear_song,
        name='crear_songs'
    ),
    path(
        'canciones/',
        views.music,
        name='songs'
    ),
]