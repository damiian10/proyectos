from django.db import models

# Create your models here.
class Direccion(models.Model):
    calle = models.CharField(max_length=50)
    no_calle = models.IntegerField()
    pais = models.CharField(max_length=100)
    predeterminada = models.BooleanField(default=True)

    def __str__(self):
        return f'id: {self.id}, pais: {self.pais}, calle: {self.calle}'

class Curso(models.Model):
    nombrecurso = models.CharField(max_length=255)
    aula = models.CharField(max_length=5)
    semestre = models.CharField(max_length=5)
    no_horas = models.IntegerField()
    modalidad = models.CharField(max_length=50)
    nivel = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, default='Principal')
    predeterminada = models.BooleanField(default=True)

    def __str__(self):
        return f'id: {self.id}, nombrecurso: {self.nombrecurso}, aula: {self.aula} , semestre: {self.semestre}, modalidad: {self.modalidad} , nivel: {self.nivel}'

class Tutor (models.Model):
    nombretutor =  models.CharField(max_length=255)
    apellidotutor =  models.CharField(max_length=255)
    titulo = models.CharField(max_length=5)
    email = models.CharField(max_length=255)
    predeterminada = models.BooleanField(default=True)

    def __str__(self):
        return f'id: {self.id}, tutor: {self.apellidotutor} {self.nombretutor}, titulo : {self.titulo }'

class Estudiante(models.Model):
    nombre = models.CharField(max_length=255)
    apellido = models.CharField(max_length=255)
    genero = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    email = models.CharField(max_length=255)
    direccion = models.ForeignKey(Direccion, on_delete=models.SET_NULL, null=True)
    curso = models.ForeignKey(Curso, on_delete=models.SET_NULL, null=True)
    tutor = models.ForeignKey(Tutor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f'id: {self.id}, nombre: {self.apellido} {self.nombre}'


