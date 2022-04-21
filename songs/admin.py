from django.contrib import admin

# Register your models here.
from .models import Song

class SongAdmin(admin.ModelAdmin):
    list_display = ("artist", "title",)

admin.site.register(Song, SongAdmin)