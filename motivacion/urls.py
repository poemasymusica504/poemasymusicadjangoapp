from django.contrib import admin
from django.urls import path
from . import views

app_name = 'poemos_app'

urlpatterns = [
    path(
        'poemas_de_motivación/', 
        views.poemo,
        name='poemos'
        ),
    path(
        'poemas_de_motivación/<int:poemo_id>',
        views.poemo_detail,
        name='poemo_detail'
    ),
    path(
        'poemas_de_motivación/crear/poema',
        views.crear_poemo,
        name='crear_poemo'
    )
]