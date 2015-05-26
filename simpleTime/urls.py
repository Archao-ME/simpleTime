from django.conf.urls import include, url
from django.contrib import admin
from entry.views import entry,upload,person,article,login,logoutView,upload
from entry.views import articleList
from getRank.views import getRank
from getRank.views import getRankDate
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
    url('^entry/list/$',articleList),
    url('^getRank/(\d{1,10})',getRank),
    url('^getRank/api/week/(\d{1,10})/(\d{8})',getRankDate),
]
