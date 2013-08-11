#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from geraldo import Report, ReportBand, ObjectValue, SystemField, BAND_WIDTH, Label, ReportGroup
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_CENTER

class ProgramacaoReport(Report):
    title = u'Programação Fenalivre'
    author = u'Éverton R. Auler'

    page_size = A4
    margin_left = 0.5*cm
    margin_top = 0.5*cm
    margin_right = 0.5*cm
    margin_bottom = 0.5*cm

    class band_detail(ReportBand):
        height = 0.5*cm
        elements=(
            ObjectValue(attribute_name='inicio', left=1*cm, get_value=lambda instance: (instance.inicio.strftime("%H:%M"))),
            ObjectValue(attribute_name='termino', left=2.5*cm, get_value=lambda instance: (instance.inicio.strftime("%H:%M"))),
            ObjectValue(attribute_name='titulo', left=5*cm),
            ObjectValue(attribute_name='palestrante', left=12*cm, get_value=lambda instance: (instance.getPalestrante())),
            ObjectValue(attribute_name='sala', left=16*cm),
        )

    class band_page_header(ReportBand):
        height = 2*cm
        elements = [
            SystemField(expression='%(report_title)s', top=0.1*cm, left=0, width=BAND_WIDTH,
                        style={'fontName': 'Helvetica-Bold', 'fontSize': 14, 'alignment': TA_CENTER}),
            Label(text= u"Início",     top=1.3*cm, left=1*cm),
            Label(text=u"Término",     top=1.3*cm, left=2.5*cm),
            Label(text=u"Título",      top=1.3*cm, left=5*cm),
            Label(text=u"Palestrante", top=1.3*cm, left=12*cm),
            Label(text=u"Sala",        top=1.3*cm, left=16*cm),
        ]
        borders = {'bottom': True}

    groups = [
        ReportGroup(attribute_name = 'tipo',
                    band_header = ReportBand(
                        height = 0.7*cm,
                        elements = [
                            ObjectValue(attribute_name='tipo', left=0, top=0.1*cm, width=20*cm,
                                        get_value=lambda instance: (instance.get_tipo_display()),
                                        style={'fontName': 'Helvetica-Bold', 'fontSize': 12})
                        ],
                        borders = {'bottom': True},
                    )
        ),
    ]
