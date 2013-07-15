#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.ForeignKey(User)
    instituicao = models.CharField(u'Instituição de Ensino', max_length=100, blank=True)
    curso = models.CharField(u'Curso', max_length=100, blank=True)
    profissao = models.CharField(u'Profissão',max_length=100, blank=True)
    cidade = models.CharField(u'Cidade',max_length=100, blank=True)
    estado = models.CharField(u'Estado',max_length=2, blank=True)
    
    class Meta():
        abstract = True
    
    def __unicode__(self):
        return "%s %s" % (self.user.first_name, self.user.last_name)
    
class Participante(Profile):
    pass
    
class Palestrante (Profile):
    pass