from pagedown.widgets import AdminPagedownWidget
from django import forms
from models import Article
from pagedown.widgets import PagedownWidget

class ArticleForm(forms.ModelForm):
    content_markdown = forms.CharField(widget=AdminPagedownWidget())
    class Meta:
        model = Article
        fields = '__all__'

class ArticleFormPerson(forms.ModelForm):

    title = forms.CharField(
        required=True,
        label = u'Title',
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
            }
        ))

    content_markdown = forms.CharField(
        required = True,

        widget=PagedownWidget(
            css=('/static/css/markdown-css.css','/static/css/custom.css'),
            attrs={
                'class':'form-control',
            }
        ))

    content_markup = forms.CharField(
        widget = forms.HiddenInput(
            )
        )
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

    class Meta:
        model = Article
        fields = '__all__'

class LoginForm(forms.Form):  
    username = forms.CharField(
        required=True,  
        label=u"username",
        error_messages={'required': 'input username'},
        widget=forms.TextInput(
            attrs={
                'placeholder':u"username",
                'class':'form-control',
            }
        ),
    ) 
    password = forms.CharField(
        required=True,
        label=u"password",
        error_messages={'required': u'input password'},
        widget=forms.PasswordInput(
            attrs={
                'placeholder':u"password",
                'class':'form-control',
            }
        ),
    )
    def clean(self):
        cleaned_data = super(LoginForm, self).clean()



