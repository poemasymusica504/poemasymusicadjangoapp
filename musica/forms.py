from django import forms
from .models import Music


class MusicForm(forms.ModelForm):
    class Meta:
        model = Music
        fields = ['nombre', 'letra', 'url', 'img']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control bg-info-subtle mx-auto p-2', 'placeholder': 'Escribe el nombre de la canción'}),
            'letra': forms.TextInput(attrs={'class': 'form-control bg-info-subtle mx-auto p-2', 'placeholder': 'Escribe la letra de la canción' }),
            'img': forms.TextInput(attrs={'class': 'form-control bg-info-subtle mx-auto p-2', 'placeholder': 'Ingresa la URL de la imagen' }),
            'url': forms.URLInput(attrs={'class': 'form-control bg-info-subtle mx-auto p-2', 'placeholder': 'Ingresa la URL'})
        }