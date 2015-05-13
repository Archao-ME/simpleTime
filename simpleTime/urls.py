from django.conf.urls import include, url
from django.contrib import admin
from entry.views import entry
from entry.views import person
from entry.views import article
from entry.views import login
from entry.views import logoutView
from entry.views import upload
urlpatterns = [
    # Examples:
    # url(r'^$', 'simpleTime.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url('^entry/$',entry),
    url('^$',entry),
    url('^entry/write/$',person),
    url('^entry/(\d{1,6})',article),
    url('^entry/login/',login),
    url('^entry/logout/$',logoutView),
    url('^entry/upload/$',upload),
    
]
