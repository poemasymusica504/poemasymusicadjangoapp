from django import forms
from .models import Poema

class PoemaForm(forms.ModelForm):
    class Meta:
        model = Poema
        fields = ['escritor', 'titulo', 'descripcion', 'poema_text', 'img']
        widgets = {
            'escritor': forms.TextInput(attrs={'class': 'form-control bg-info-subtle mx-auto p-2', 'placeholder': 'Escribe el nombre del escritor'}),
            'titulo': forms.TextInput(attrs={'class': 'form-control bg-info-subtle mx-auto p-2', 'placeholder': 'Escribe el titulo' }),
            'descripcion': forms.Textarea(attrs={'class': 'form-control bg-info-subtle mx-auto p-2', 'placeholder': 'Escribe la descripción' }),
            'poema_text': forms.Textarea(attrs={'class': 'form-control bg-info-subtle mx-auto p-2', 'placeholder': 'Escribe el poema' }),
            'img': forms.TextInput(attrs={'class': 'form-control bg-info-subtle mx-auto p-2', 'placeholder': 'Url de la imagen' }),
        } 