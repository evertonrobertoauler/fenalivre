from django.http import HttpResponse, HttpResponseRedirect
from geraldo.generators import PDFGenerator
from .models import Programacao
from .report import ProgramacaoReport

def home_page(request):
    return HttpResponseRedirect("inicio")

def pdf(request):
    resp = HttpResponse(mimetype='application/pdf')

    report = ProgramacaoReport(queryset=Programacao.objects.all())
    report.generate_by(PDFGenerator, filename=resp)

    return resp