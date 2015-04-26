from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from markdown import markdown

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=15)

class Article(models.Model):
    title = models.CharField(max_length=50)
    tag = models.ManyToManyField(Tag,blank=True)
    content_markdown = models.TextField()
    content_markup = models.TextField(blank=True)
    publish_date = models.DateField(auto_now=True)
    def __unicode__(self):
        return "%s" % (self.title,)