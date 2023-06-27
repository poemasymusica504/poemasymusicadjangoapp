from django.shortcuts import render, redirect, get_object_or_404
from .forms import PoemaForm
from .models import Poema
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
# Create your views here.


def crear_poema(request):

    if request.method == 'GET':
        return render(request, 'crear_poema.html', {
            'form': PoemaForm
        })
    else:
        try:
            form = PoemaForm(request.POST)
            new_poema = form.save(commit=False)
            new_poema.user = request.user
            new_poema.save()
            return redirect('poemas_app:poemas')
        except ValueError:
            return render(request, 'crear_poema.html', {
                'form': PoemaForm,
                'error': 'Ingresar información valida o hay un campo faltante'
            })

def poemas(request):
    poema_list = Poema.objects.all().order_by('-fecha')

    return render(request, 'amor.html', {
        'poema_list': poema_list
    })

def poema_detail(request, poema_id):
    poema = get_object_or_404(Poema, pk=poema_id)
    return render(request, 'poema_detail.html', {
        'poema': poema
    })

def registrarse(request):
    if request.method == 'GET':
        return render(request, 'registrarse.html', {
            'formUser': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                #registro de usuarios
                user = User.objects.create_superuser(
                    username=request.POST["username"],
                    password=request.POST["password1"],
                )
                user.save()
                return redirect('login')
            except IntegrityError:
                return render(request, "registrarse.html", {
                    "formreuser": UserCreationForm,
                    "error": "El usuario ya existe"
                })
    return render(request, "registrarse.html", {
        "formreuser": UserCreationForm,
        "error":"Las contraseñas no coinciden"
    })

def desconectar(request):
    logout(request)
    return redirect('poemas_app:poemas')

def ingresar(request):
    if request.method == 'GET':
        return render(request, 'login.html',{
        'formin': AuthenticationForm
        })
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, "login.html", {
                'formin': AuthenticationForm,
                'error': 'Usuario o contraseña incorrecta'
            })
        else:
            login(request, user)
            return redirect('poemas_app:poemas')