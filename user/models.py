#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

SIM_NAO = ((True,  u'Sim'),
           (False, u'Não'))

class Profile(models.Model):
    user = models.OneToOneField(User)
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