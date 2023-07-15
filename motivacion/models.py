from django.db import models

# Create your models here.
import datetime
from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField

# Create your models here.
class Poemo(models.Model):
    escritor = models.CharField(max_length=50)
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=250)
    poema_text = models.TextField(max_length=5000)
    img = models.CharField(max_length=999)
    fecha = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.titulo