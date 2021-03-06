#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import User
from mezzanine.pages.models import Page

TIPO = ((1, u'Palestra'),
        (2, u'Intervalo'),
        (3, u'Descontração'),
        (4, u'Oficina'))

SIM_NAO = ((True,  u'Sim'),
           (False, u'Não'))


class Profile(models.Model):
    user = models.OneToOneField(User)
    instituicao = models.CharField(u'Instituição de Ensino', max_length=100, blank=True)
    curso = models.CharField(u'Curso', max_length=100, blank=True)
    profissao = models.CharField(u'Profissão',max_length=100, blank=True)
    cidade_uf = models.CharField(u'Cidade / UF',max_length=100, blank=True)
    
    class Meta():
        abstract = True
    
    def __unicode__(self):
        return self.user.first_name and "%s %s" % (self.user.first_name, self.user.last_name) or self.user.email or self.user.username

    
class Palestrante (Profile):
    pass


class ParticipanteManager(models.Manager):
    def get_query_set(self):
        return super(ParticipanteManager, self).get_query_set().exclude(user__pk__in=Palestrante.objects.all().values_list('user__pk', flat=True))
        
class Participante(Profile):
    estara_presente = models.BooleanField(u'Estará presente', default=True, choices=SIM_NAO)
    esteve_presente = models.BooleanField(u'Esteve realmente presente', default=False, choices=SIM_NAO)
    objects = ParticipanteManager()
    
class ProgramacaoPage(Page):
    pass

class NovoLink(Page):
    new_tab = models.BooleanField("Abrir em nova Aba")
    
class Programacao(models.Model):
    inicio = models.TimeField(u'Início')
    termino = models.TimeField(u'Fim')
    titulo = models.CharField(u'Titulo', max_length=40)
    descricao = models.TextField(u'Descrição', null=True, blank=True)
    palestrante = models.ForeignKey(Palestrante, null=True, blank=True)
    tipo = models.SmallIntegerField(u'Tipo', choices=TIPO)
    sala = models.CharField(u'Sala', max_length=20, null=True, blank=True)
    page = models.ForeignKey(ProgramacaoPage)

    def __unicode__(self):
        return self.titulo
    
    def getInicio(self):
        return self.inicio.strftime("%H:%M")
    
    def getTermino(self):
        return self.termino.strftime("%H:%M")
    
    def getPalestrante(self):
        return self.palestrante or " "
    
    def getTitulo(self):
        return " - " . join([ds for ds in [self.titulo, self.descricao] if ds])
    
    class Meta:
        verbose_name = u"Programação"
        verbose_name_plural = u"Programações"
        ordering = ['inicio', 'termino', 'titulo']