from django.contrib import admin
from programacao.models import Programacao

class ProgramacaoAdmin(admin.ModelAdmin):
    list_display = ('inicio', 'termino', 'titulo', 'sala', 'palestrante')
    list_display_links = ('inicio', 'termino', 'titulo', 'sala', 'palestrante')

admin.site.register(Programacao, ProgramacaoAdmin)