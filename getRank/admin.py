from django.contrib import admin
from models import SongList
from models import RankID
# Register your models here.

class SongListAdmin(admin.ModelAdmin):
    list_display=('song_ID','song_Name','user_ID','score','date')
class RankIDAdmin(admin.ModelAdmin):
    list_display=('rank_ID','date')
admin.site.register(SongList,SongListAdmin)
admin.site.register(RankID,RankIDAdmin)