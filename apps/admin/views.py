from django.shortcuts import render
import json
from django.core import serializers
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from apps.gestion_mascotas.models import mascota
from datetime import datetime

from django.db.models.functions import Coalesce
from django.db.models import Sum

from django.views.generic import TemplateView

from django.views import View

from django.http import JsonResponse, HttpResponse, HttpResponseRedirect

from django.urls import reverse_lazy



# print to pdf



import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.staticfiles import finders

# Create your views here.


# def chart2(self):
#     qs = mascota.objects.all()
#     datos_mensuales = serialize('json', qs, fields = 'fecha_rescate' )
#     total_datos = datos_mensuales.count('pk')
#     return total



def chart1(request):
    adopcion_data = mascota.objects.filter(estado__icontains='En adopcion').count()
    custodia_data = mascota.objects.filter(estado__icontains='En custodia').count()
    tratamiento_data = mascota.objects.filter(estado__icontains='En tratamiento').count()
    adoptado_data = mascota.objects.filter(estado__icontains='Adoptado').count()
    qs = mascota.objects.all()
    datos_mensuales = serialize('json', qs, fields = 'fecha_rescate' )
    total_datos = datos_mensuales.count('pk')
    context = {
        "json" : adopcion_data,
        "json2": custodia_data,
        "json3": tratamiento_data,
        "json4": adoptado_data,
        "json5": datos_mensuales,
        "json6": total_datos,

        }
    return render(request, 'Graficos/charts.html', context)


def chart_poblacion(request):


    data = []

    hembras = mascota.objects.filter(sexo__icontains = 'Hembra')
    machos = mascota.objects.filter(sexo__icontains = 'Macho')
    gatos_hembra = hembras.objects.filter(especie__icontains = 'Gato').cont('pk')
    gatos_macho = machos.objects.filter(especie__icontains = 'Gato').cont('pk')
    perros_hembra = hembras.objects.filter(especie__icontains = 'Perro').cont('pk')
    perros_macho = machos.objects.filter(especie__icontains = 'Perro').cont('pk')


    context = {

        'total_gatos_hembras': gatos_hembra,
        'total_gatos_machos':  gatos_macho,
        'total_perros_hembras':   perros_hembra,
        'total_perros_machos':  perros_macho,
    }
    return JsonResponse()
        






def report (request):
        adopcion_data = mascota.objects.filter(estado__icontains='En adopcion').count()
        custodia_data = mascota.objects.filter(estado__icontains='En custodia').count()
        tratamiento_data = mascota.objects.filter(estado__icontains='En tratamiento').count()
        adoptado_data = mascota.objects.filter(estado__icontains='Adoptado').count()
        qs = mascota.objects.all()
        datos_mensuales = serialize('json', qs, fields = 'fecha_rescate' )
        total_datos = datos_mensuales.count('pk')

        gatos = mascota.objects.filter(especie__icontains = 'Gato').count()
        perros = mascota.objects.filter(especie__icontains = 'Perro').count()
        total_mascotas = perros + gatos

        hembras = mascota.objects.filter(sexo__icontains = 'Hembra')
        machos = mascota.objects.filter(sexo__icontains = 'Macho')
        gatos_hembra = hembras.filter(especie__icontains = 'Gato').count()
        gatos_macho = machos.filter(especie__icontains = 'Gato').count()
        perros_hembra = hembras.filter(especie__icontains = 'Perro').count()
        perros_macho = machos.filter(especie__icontains = 'Perro').count()
        context = {
            "json" : adopcion_data,
            "json2": custodia_data,
            "json3": tratamiento_data,
            "json4": adoptado_data,
            "json5": datos_mensuales,
            "json6": total_datos,
            'total_gatos': gatos,
            'total_perros': perros,
            'total_gatos_hembras': gatos_hembra,
            'total_gatos_machos':  gatos_macho,
            'total_perros_hembras':   perros_hembra,
            'total_perros_machos':  perros_macho,
            'total_mascotas' : total_mascotas,
        }
        return render(request,'Graficos/reportes.html', context)

    



  
# class DashboardView(TemplateView):
#     template_name = "Graficos/charts2.html"

#     def get_report_adoption_months(self):
#         data = []
#         try:
#             year = datetime.now().year
#             for m in range(1,13):
#                 total = mascota.objects.filter(fecha_rescate__year = year,fecha_rescate__month = m).aggregate(r=Coalesce(Sum('fecha_rescate'), 0)).get('r')
#                 data.append(float(total))
#         except:
#             pass
#         return data

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context["report_adoption_months"] = self.get_report_adoption_months()
#         return context


def DashboardView(request):
    return render(request, 'Graficos/charts2.html')

def line_chart(request):
    labels = []
    data = []

    queryset = mascota.objects.values('fecha_rescate').annotate(mascotas_mes=Sum('pk')).order_by('-mascotas_mes')
    for entry in queryset:
        labels.append(entry['fecha_rescate'])
        data.append(entry['mascotas_mes'])
        return JsonResponse(data={
            'labels': labels,
            'data': data,
        })



# Vista para la creaciond de reporte pdf


class report_pdf_view(View):

    def link_callback(self, uri, rel):
            """
            Convert HTML URIs to absolute system paths so xhtml2pdf can access those
            resources
            """
            result = finders.find(uri)
            if result:
                    if not isinstance(result, (list, tuple)):
                            result = [result]
                    result = list(os.path.realpath(path) for path in result)
                    path=result[0]
            else:
                    sUrl = settings.STATIC_URL        # Typically /static/
                    sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
                    mUrl = settings.MEDIA_URL         # Typically /media/
                    mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

                    if uri.startswith(mUrl):
                            path = os.path.join(mRoot, uri.replace(mUrl, ""))
                    elif uri.startswith(sUrl):
                            path = os.path.join(sRoot, uri.replace(sUrl, ""))
                    else:
                            return uri

            # make sure that file exists
            if not os.path.isfile(path):
                    raise Exception(
                            'media URI must start with %s or %s' % (sUrl, mUrl)
                    )
            return path

    def get(self, request, *args, **kwargs):
        try:
            template = get_template('Graficos/prueba.html')
            context = {'title': 'pdf report'}
            html = template.render(context)
            response = HttpResponse(content_type='application/pdf')
            # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
            # create a pdf
            pisa_status = pisa.CreatePDF(
                html, dest=response)
            return response
        except:
            pass
        return HttpResponseRedirect(reverse_lazy('reportes'))