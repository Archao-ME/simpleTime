from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import Http404, HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
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
        mysong = get163Rank.Get163Rank(ID)
        mysong.GetHtml()
        mysong.WeekDic()
        mysong.SaveWeek()
        songList = SongList.objects.filter(user_ID = id,date=today)

    return render_to_response('getRank.html',{'songList':songList},context_instance = RequestContext(request))
