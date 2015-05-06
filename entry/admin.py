from django.contrib import admin
from django import forms
from pagedown.widgets import AdminPagedownWidget
from models import Article,Tag,UploadFile
from forms import ArticleForm
from markdown import markdown
from forms import UploadFileForm

# Register your models here.

class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    fields = ('title','tag','author','content_markdown','content_markup')
    list_display = ('id','title','author','publish_date')
    def save_model(self, request, obj, form, change):
        obj.content_markup = markdown(obj.content_markdown)
        obj.save()
class FilesAdmin(admin.ModelAdmin):
    form = UploadFileForm

admin.site.register(UploadFile,FilesAdmin)
admin.site.register(Tag,TagAdmin)
admin.site.register(Article,ArticleAdmin)

