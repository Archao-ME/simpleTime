from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
import json
import get163Rank
import datetime 
from models import SongList

# Create your views here.

def getRank(request,ID):
    ISOFORMAT='%Y%m%d'
    today = datetime.date.today().strftime(ISOFORMAT)
    id = ID
    songList = SongList.objects.filter(user_ID = id,date=today)
    if not songList :
        mysong = get163Rank.Get163Rank()
        mysong.SaveWeek(ID)
        songList = SongList.objects.filter(user_ID = id,date=today)

    return render_to_response('getRank.html',{'songList':songList,'user_ID':id},context_instance = RequestContext(request))
def loopID(request):
    songRank = get163Rank.Get163Rank()
    songRank.LoopID()
    return HttpResponse("LoopID OK!")

def getRankDate(request,ID,date):
    ISOFORMAT='%Y%m%d'
    id = ID 
    songList = SongList.objects.filter(user_ID = id,date=date)
    if not songList :
        return HttpResponse("500")
    else:
        songDic = {}
        for song in songList:
            songDic[song.song_ID] = {"name":song.song_Name,"score":song.score}

        songJson = json.dumps(songDic)
        print songJson
        return render_to_response('getRankAPI.html',{'songList':songList},context_instance = RequestContext(request))


