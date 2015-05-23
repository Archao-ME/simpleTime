from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class SongList(models.Model):
    song_ID = models.IntegerField()
    song_Name = models.CharField(max_length=20)
    user_ID =models.IntegerField()
    date = models.CharField(max_length=12)
    score = models.IntegerField()

    def __unicode__(self):
        return "%s" % (self.song_ID)

