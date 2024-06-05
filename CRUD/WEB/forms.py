from django import forms
from .models import Empleado, Departamento

class EmpleadoForm(forms.ModelForm):
    departamento = forms.ModelChoiceField(queryset=Departamento.objects.all(), empty_label="Seleccione un departamento")
    #forms.ModelChoiceField(queryset=Departamento.objects.all()) 
    #crea un campo de formulario que permite seleccionar un objeto de un queryset, en este caso Departamento.objects.all()
    class Meta:
        model = Empleado
        fields = ['nombre_empleado', 'apellido_empleado', 'email_empleado', 'edad_empleado', 'genero_empleado', 'salario_empleado','departamento']
        
class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre_departamento', 'ubicacion']