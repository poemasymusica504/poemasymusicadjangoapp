from django.contrib import admin
from .models import Poemo
# Register your models here.

@admin.register(Poemo)

class PoemoAdmin(admin.ModelAdmin):
    list_display = ('id','escritor','titulo','fecha')
    search_fields = ('id','escritor','titulo')