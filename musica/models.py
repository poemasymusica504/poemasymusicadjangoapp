from django.db import models

# Create your models here.
from django.db import models

class Music(models.Model):
    nombre = models.CharField(max_length=50)
    letra = models.CharField(max_length=500)
    img = models.CharField(blank=True, max_length=999)
    url = models.URLField(blank=True)
    fecha = models.DateField(auto_now_add=True, null=True)

    def __str__(self):
        return self.nombre
    