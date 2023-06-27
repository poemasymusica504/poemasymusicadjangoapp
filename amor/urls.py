from django.contrib import admin
from django.urls import path
from . import views

app_name = 'poemas_app'

urlpatterns = [
    path(
        'crear_poema/',
        views.crear_poema,
        name='crear_poema'
    ),
    path(
        '',
        views.poemas, 
        name='poemas'
    ),
    path(
        '<int:poema_id>/',
        views.poema_detail,
        name='poema_detail'
    ),
    path(
        'registrarse/',
        views.registrarse,
        name='sing_in'
    ),
    path(
        'login/',
        views.ingresar,
        name='login'
    ),
    path(
        'desconectar/',
        views.desconectar,
        name='desconectar'
    )
]