from django.conf.urls import include, url
from django.contrib import admin
from entry.views import entry
from entry.views import person
from entry.views import article
urlpatterns = [
    # Examples:
    # url(r'^$', 'simpleTime.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    
    url(r'^admin/', include(admin.site.urls)),
    url('^entry/$',entry),
    url('^entry/person/$',person),
    url('^entry/(\d{1,6})',article),
]
