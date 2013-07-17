from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'user/login.html'}),
    url(r'^registro/$', 'user.views.registro'),
    url(r'^logout/$', 'user.views.logout'),
    url(r'^profile/$', 'user.views.profile'),
)
