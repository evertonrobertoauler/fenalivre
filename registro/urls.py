from django.conf.urls import patterns, url, include
from django.views.generic.base import TemplateView

from registration.backends.default.views import ActivationView
from registration.backends.default.views import RegistrationView
from registro.forms import UserCreationForm

urlpatterns = patterns('',
    url(r'^ativacao/completa/$',
        TemplateView.as_view(template_name='registration/ativacao_completa.html'),
        name='registration_activation_complete'),
    url(r'^ativacao/(?P<activation_key>\w+)/$',
        ActivationView.as_view(template_name='registration/ativacao.html'),
        name='registration_activate'),
                       
    url(r'^registrar/$',
        RegistrationView.as_view(template_name='registration/registro.html', form_class=UserCreationForm),
        name='registration_register'),
    url(r'^registro/concluido/$',
        TemplateView.as_view(template_name='registration/registro_concluido.html'),
        name='registration_complete'),
    url(r'^registro/encerrado/$',
        TemplateView.as_view(template_name='registration/registro_encerrado.html'),
        name='registration_disallowed'),
    (r'', include('registration.auth_urls')),
)