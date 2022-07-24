from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.}
from django.template import loader

from estudiante.models import Estudiante


def bienvenidos(request):
    cantidad = Estudiante.objects.count()
    estudiantes = Estudiante.objects.order_by('apellido')
    mensaje = {'cantidad': cantidad, 'estudiantes':estudiantes}
    pagina = loader.get_template('bienvenidos.html')
    return HttpResponse(pagina.render(mensaje, request))