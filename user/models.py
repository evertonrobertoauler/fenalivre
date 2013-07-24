#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin, SiteProfileNotAvailable
from django.utils.translation import ugettext_lazy as _
import warnings
from django.utils import timezone
from django.core.exceptions import ImproperlyConfigured
from django.core.mail import send_mail
from django.utils.http import urlquote
from django.conf import settings

SIM_NAO = ((True,  u'Sim'),
           (False, u'Não'))


class FenalivreUserManager(UserManager):
    """
    classe é uma adaptação do UserManager do Django
    """
    def create_user(self, username, email=None, password=None, **extra_fields):
        return super(FenalivreUserManager, self).create_user(username = email or username, email=email, password=password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        return super(FenalivreUserManager, self).create_superuser(email, email, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    """
    classe é uma adaptação do Model User do Django
    """
    username = models.EmailField(_('email'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    email = models.EmailField(_('email'), unique=True)
    is_staff = models.BooleanField(_('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin '
                    'site.'))
    is_active = models.BooleanField(_('active'), default=True,
        help_text=_('Designates whether this user should be treated as '
                    'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = FenalivreUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_absolute_url(self):
        return "/users/%s/" % urlquote(self.username)

    def get_full_name(self):
        """
        Returns the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        "Returns the short name for the user."
        return self.first_name

    def email_user(self, subject, message, from_email=None):
        """
        Sends an email to this User.
        """
        send_mail(subject, message, from_email, [self.email])

    def get_profile(self):
        """
        Returns site-specific profile for this user. Raises
        SiteProfileNotAvailable if this site does not allow profiles.
        """
        warnings.warn("The use of AUTH_PROFILE_MODULE to define user profiles has been deprecated.",
            PendingDeprecationWarning)
        if not hasattr(self, '_profile_cache'):
            if not getattr(settings, 'AUTH_PROFILE_MODULE', False):
                raise SiteProfileNotAvailable(
                    'You need to set AUTH_PROFILE_MODULE in your project '
                    'settings')
            try:
                app_label, model_name = settings.AUTH_PROFILE_MODULE.split('.')
            except ValueError:
                raise SiteProfileNotAvailable(
                    'app_label and model_name should be separated by a dot in '
                    'the AUTH_PROFILE_MODULE setting')
            try:
                model = models.get_model(app_label, model_name)
                if model is None:
                    raise SiteProfileNotAvailable(
                        'Unable to load the profile model, check '
                        'AUTH_PROFILE_MODULE in your project settings')
                self._profile_cache = model._default_manager.using(
                                   self._state.db).get(user__id__exact=self.id)
                self._profile_cache.user = self
            except (ImportError, ImproperlyConfigured):
                raise SiteProfileNotAvailable
        return self._profile_cache



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL)
    instituicao = models.CharField(u'Instituição de Ensino', max_length=100, blank=True)
    curso = models.CharField(u'Curso', max_length=100, blank=True)
    profissao = models.CharField(u'Profissão',max_length=100, blank=True)
    cidade = models.CharField(u'Cidade',max_length=100, blank=True)
    estado = models.CharField(u'Estado',max_length=2, blank=True)
    
    class Meta():
        abstract = True
    
    def __unicode__(self):
        return self.user.first_name and "%s %s" % (self.user.first_name, self.user.last_name) or self.user.username
    
    def get_cidade_estado(self):
        return " / ".join([val for val in [self.cidade, self.estado] if val])
    
class Participante(Profile):
    estara_presente = models.BooleanField(u'Estará presente', default=True, choices=SIM_NAO)
    esteve_presente = models.BooleanField(u'Esteve realmente presente', default=False, choices=SIM_NAO)
    
class Palestrante (Profile):
    pass