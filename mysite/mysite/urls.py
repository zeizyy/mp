from django.conf.urls import patterns, include, url
from django.contrib import admin

from mp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^mp/$', views.index, name='index'),
    url(r'^mp/all/$', views.all, name='all'),
    url(r'^mp/(?P<mentor_id>\d+)/$', views.mentor, name='mentor'),
    url(r'^mp/home/$', views.home, name='home'),
    url(r'^mp/major/$', views.major, name='major'),
    url(r'^mp/year/$', views.year, name='year'),
)
