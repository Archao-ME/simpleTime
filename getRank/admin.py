from django.contrib import admin
from models import SongList
# Register your models here.

class SongListAdmin(admin.ModelAdmin):
    list_display=('song_ID','song_Name','user_ID','score','date')

admin.site.register(SongList,SongListAdmin)