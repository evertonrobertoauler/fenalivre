from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^social_auth/login/', include('social_auth.urls')),
    url(r'^user/', include('user.urls')),
    
    url(r'^$', 'user.views.login'),
)
