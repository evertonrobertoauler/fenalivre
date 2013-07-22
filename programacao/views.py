from django.shortcuts import render_to_response
from django.template.context import RequestContext
from programacao.models import Palestra, Oficina

def index(request):
    p = Palestra.objects.all().order_by('inicio', 'titulo')
    o = Oficina.objects.all().order_by('inicio', 'titulo')
    
    return render_to_response('programacao.html', {'palestras': p, 'oficinas': o},context_instance=RequestContext(request))