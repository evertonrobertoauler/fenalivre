from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login/$', 'user.views.login'),
    url(r'^logout/$', 'user.views.logout'),
    url(r'^profile/$', 'user.views.profile'),
)
