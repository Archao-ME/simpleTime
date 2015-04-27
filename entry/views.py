from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django import forms
from django.contrib import auth  
from django.contrib import messages 
from django.contrib.auth.models import User
from models import Article
from django.template import RequestContext
from django.shortcuts import render_to_response
from models import Article

# Create your views here.

def entry(request):
    articleList = Article.objects.all()

    return render_to_response('index.html',{'articleList':articleList},context_instance = RequestContext(request))