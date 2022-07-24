from django.contrib import admin

# Register your models here.
from estudiante.models import Estudiante, Tutor, Curso, Direccion

admin.site.register(Estudiante)
admin.site.register(Tutor)
admin.site.register(Curso)
admin.site.register(Direccion)