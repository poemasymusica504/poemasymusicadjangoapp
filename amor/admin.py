from django.contrib import admin
from .models import Poema
# Register your models here.

@admin.register(Poema)

class PoemaAdmin(admin.ModelAdmin):
    list_display = ('id','escritor','titulo','fecha')
    search_fields = ('id','escritor','titulo')

    list_display_links = ('escritor')

    