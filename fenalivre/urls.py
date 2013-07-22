from django.conf.urls import patterns, include, url
from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail

class RegistrationViewUniqueEmail(RegistrationView):
    form_class = RegistrationFormUniqueEmail
       
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'user.views.index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^social_auth/login/', include('social_auth.urls')),
    url(r'^user/', include('user.urls')),
    url(r'^registro/', include('registro.urls')),
    url(r'^programacao/', 'programacao.views.index'),
)
