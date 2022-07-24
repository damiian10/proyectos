from django.forms import ModelForm, EmailInput

from estudiante.models import Estudiante


class PersonaFormulario(ModelForm):
    class Meta:
        model = Estudiante
        fields = ('nombre', 'apellido', 'genero', 'email','direccion','curso')
        widgets = {
            'email': EmailInput(attrs={'type': 'email'})
        }
