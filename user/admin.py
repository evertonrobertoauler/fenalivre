from django.contrib import admin
from user.models import Palestrante, Participante, User

admin.site.register(User)
admin.site.register(Palestrante)
admin.site.register(Participante)