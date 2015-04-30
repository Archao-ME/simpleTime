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
from django import forms
from django.core.context_processors import csrf
import forms

# Create your views here.

def entry(request):
    articleList = Article.objects.order_by('-id')
    localURL = request.get_host()
    return render_to_response('index.html',{'articleList':articleList,'localURL':localURL},context_instance = RequestContext(request))

def article(request,articleID):
    article = Article.objects.get(id=articleID)

    return render_to_response('article.html',{'article':article},context_instance = RequestContext(request))
def person(request):
    if request.method == 'GET':
        articleForm = forms.ArticleFormPerson()
        return render_to_response('person.html',{'state':"GET",'articleForm':articleForm},context_instance = RequestContext(request))
    else :
        form = forms.ArticleFormPerson(request.POST)
        if form.is_valid:
            title = request.POST.get('title')
            
            content_markdown = request.POST.get('content_markdown')
            content_markup = content_markdown
            
            articleModel = Article(title=title,content_markdown=content_markdown,content_markup=content_markup)
            articleModel.save()
        return HttpResponseRedirect('127.0.0.1/entry')