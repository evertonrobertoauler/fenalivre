#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from django.contrib import admin
from mezzanine.pages.admin import PageAdmin, LinkAdmin
from .models import ProgramacaoPage, Programacao, Palestrante, Participante, NovoLink
from copy import deepcopy

# Cadastro tipo de Pagina Programacao 
class ProgramacaoInline(admin.TabularInline):
    model = Programacao

class ProgramacaoAdmin(PageAdmin):
    inlines = (ProgramacaoInline,)
    
admin.site.register(ProgramacaoPage, ProgramacaoAdmin)


# Cadastro tipo de Link com posibilidade de ser aberto em nova aba
class NovoLinkAdmin(LinkAdmin):
    fieldsets = deepcopy(LinkAdmin.fieldsets) + ((None, {"fields": ("new_tab",)}),)

admin.site.register(NovoLink, NovoLinkAdmin)


# cadastro do model para Palestrante
admin.site.register(Palestrante)

# cadastro do model para Palestrante
class ParticipanteAdmin(admin.ModelAdmin):
    ordering = ['user__first_name', 'user__last_name']
    list_display = ('__unicode__', 'estara_presente', 'esteve_presente')
    list_filter = ('estara_presente', 'esteve_presente')
    search_fields = ['user__first_name', 'user__last_name']
    
    actions = ['marcarPresenca']

    def marcarPresenca(self, request, queryset):
        queryset.update(esteve_presente=True)
    marcarPresenca.short_description = u"Marcar Presença"

admin.site.register(Participante, ParticipanteAdmin)