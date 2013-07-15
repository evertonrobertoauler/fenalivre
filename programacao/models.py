#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from django.db import models
from user.models import Palestrante

class Programacao(models.Model):
    inicio = models.TimeField(u'Hr. Início')
    termino = models.TimeField(u'Hr. Término')
    titulo = models.CharField(u'Titulo', max_length=40)
    descricao = models.TextField(u'Descrição', blank=True)
    palestrante = models.ForeignKey(Palestrante)
    
    class Meta():
        abstract = True
        
    def __unicode__(self):
        return self.titulo
    
class Palestra(Programacao):
    sala = models.CharField(u'Sala', max_length=20, default=u'Auditório')

class Oficina(Programacao):
    sala = models.CharField(u'Sala', max_length=20)