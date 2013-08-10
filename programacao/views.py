from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from programacao.models import Programacao

from programacao.report import ProgramacaoReport
from geraldo.generators import PDFGenerator

def index(request):
    return render_to_response('programacao.html', {'programacoes': Programacao.objects.all()}, 
                              context_instance=RequestContext(request))
    
def pdf(request):
    resp = HttpResponse(mimetype='application/pdf')

    report = ProgramacaoReport(queryset=Programacao.objects.all())
    report.generate_by(PDFGenerator, filename=resp)

    return resp