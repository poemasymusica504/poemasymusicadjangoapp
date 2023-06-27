from django.shortcuts import render, redirect, get_object_or_404
from .forms import PoemoForm
from .models import Poemo
# Create your views here.


def crear_poemo(request):

    if request.method == 'GET':
        return render(request, 'crear_poemo.html', {
            'form': PoemoForm
        })
    else:
        try:
            form = PoemoForm(request.POST, files=request.FILES)
            new_poemo = form.save(commit=False)
            new_poemo.save()
            return redirect('poemos_app:poemos')
        except ValueError:
            return render(request, 'crear_poemo.html', {
            'form': PoemoForm,
            'error': 'Por favor ingresa todos los campos'
        })

def poemo(request):
    poemo_list = Poemo.objects.all().order_by('-fecha')

    return render(request, "motivacion.html", {
        "poemo_list": poemo_list
    }) 

def poemo_detail(request, poemo_id):
    poemo = get_object_or_404(Poemo, pk=poemo_id)
    return render(request, 'poemo_detail.html', {
        'poemo': poemo
    })
