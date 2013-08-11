from django.contrib import admin
from mezzanine.pages.admin import PageAdmin
from .models import ProgramacaoPage, Programacao

class ProgramacaoInline(admin.TabularInline):
    model = Programacao

class ProgramacaoAdmin(PageAdmin):
    inlines = (ProgramacaoInline,)

admin.site.register(ProgramacaoPage, ProgramacaoAdmin)