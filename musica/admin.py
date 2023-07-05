from django.contrib import admin
from .models import Music
# Register your models here.

@admin.register(Music)

class MusicAdmin(admin.ModelAdmin):
    list_display = ('id','nombre','url','fecha')
    search_fields = ('id','nombre')