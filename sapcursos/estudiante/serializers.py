from rest_framework import serializers

from estudiante.models import Estudiante, Tutor, Curso, Direccion


class EstudianteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudiante
        fields = ['url' , 'id' , 'nombre', 'apellido', 'genero','telefono', 'email' ]

class TutorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tutor
        fields = ['url', 'id' , 'nombretutor' , 'apellidotutor' , 'titulo', 'email', 'predeterminada' ]

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['url', 'id' , 'nombrecurso' , 'aula' , 'semestre', 'no_horas', 'modalidad' , 'nivel' , 'tipo', 'predeterminada' ]

class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = ['url' , 'id' , 'calle', 'no_calle', 'pais','predeterminada' ]