#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from django.db import models
from user.models import Palestrante

TIPO = ((1, u'Palestra'),
        (2, u'Intervalo'),
        (3, u'Descontração'),
        (4, u'Oficina'))

class Programacao(models.Model):
    inicio = models.TimeField(u'Hr. Início')
    termino = models.TimeField(u'Hr. Término')
    titulo = models.CharField(u'Titulo', max_length=40)
    descricao = models.TextField(u'Descrição', null=True, blank=True)
    palestrante = models.ForeignKey(Palestrante, null=True, blank=True)
    tipo = models.SmallIntegerField(u'Tipo', choices=TIPO)
    sala = models.CharField(u'Sala', max_length=20, null=True, blank=True)
      
    def __unicode__(self):
        return self.titulo
    
    class Meta:
        verbose_name = u"Programação"
        verbose_name_plural = u"Programações"
        ordering = ['inicio', 'termino', 'titulo']