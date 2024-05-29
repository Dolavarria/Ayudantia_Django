from django import forms
from .models import Empleado

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre_empleado', 'apellido_empleado', 'email_empleado', 'edad_empleado', 'genero_empleado', 'salario_empleado']