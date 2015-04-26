from pagedown.widgets import AdminPagedownWidget
from django import forms
from models import Article


class ArticleForm(forms.ModelForm):
    content_markdown = forms.CharField(widget=AdminPagedownWidget())
    class Meta:
        model = Article
        fields = '__all__'