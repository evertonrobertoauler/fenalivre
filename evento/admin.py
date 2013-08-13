from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import ProgramacaoPage, Programacao, Palestrante, Participante

class ProgramacaoInline(admin.TabularInline):
    model = Programacao

class ProgramacaoAdmin(PageAdmin):
    inlines = (ProgramacaoInline,)

admin.site.register(ProgramacaoPage, ProgramacaoAdmin)
admin.site.register(Palestrante)
admin.site.register(Participante)