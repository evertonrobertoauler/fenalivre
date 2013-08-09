from django.shortcuts import render_to_response
from django.template.context import RequestContext
from programacao.models import Programacao

def index(request):
    return render_to_response('programacao.html', {'programacoes': Programacao.objects.all()}, 
                              context_instance=RequestContext(request))