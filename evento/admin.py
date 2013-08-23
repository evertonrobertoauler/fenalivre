from django.contrib import admin
from mezzanine.pages.admin import PageAdmin, LinkAdmin
from .models import ProgramacaoPage, Programacao, Palestrante, Participante, NovoLink
from copy import deepcopy

class ProgramacaoInline(admin.TabularInline):
    model = Programacao

class ProgramacaoAdmin(PageAdmin):
    inlines = (ProgramacaoInline,)
    
class NovoLinkAdmin(LinkAdmin):
    fieldsets = deepcopy(LinkAdmin.fieldsets) + ((None, {"fields": ("new_tab",)}),)

admin.site.register(ProgramacaoPage, ProgramacaoAdmin)
admin.site.register(NovoLink, NovoLinkAdmin)
admin.site.register(Palestrante)
admin.site.register(Participante)