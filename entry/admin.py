from django.contrib import admin
from django import forms
from pagedown.widgets import AdminPagedownWidget
from models import Article,Tag
from forms import ArticleForm
from markdown import markdown
# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    fields = ('title','tag','content_markdown','content_markup')
    def save_model(self, request, obj, form, change):
        obj.content_markup = markdown(obj.content_markdown)
        obj.save()

admin.site.register(Tag,TagAdmin)
admin.site.register(Article,ArticleAdmin)

