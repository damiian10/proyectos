"""sapcursos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from estudiante.views import detalle_estudiante, nuevo_estudiante, modificar_estudiante, eliminar_estudiante, reporte_estudiantes
from webapp.views import bienvenidos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bienvenidos, name='inicio'),
    path('detalle_estudiante/<int:id>', detalle_estudiante, name= 'detalle_estudiante'),
    path('nuevo_estudiante/', nuevo_estudiante, name= 'nuevo_estudiante'),
    path('modificar_estudiante/<int:id>', modificar_estudiante, name= 'modificar_estudiante'),
    path('eliminar_estudiante/<int:id>', eliminar_estudiante, name= 'eliminar_estudiante'),
    path('reporte_estudiantes/', reporte_estudiantes, name= 'reporte_estudiantes'),
]
