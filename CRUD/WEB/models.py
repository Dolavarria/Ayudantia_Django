from django.db import models

# Create your models here.
GENERO_OPCIONES = (
    ('masculino', 'Masculino'),
    ('femenino', 'Femenino'),
    ('otro', 'Otro')
)
    #Primer campo es el valor que se guarda en la base de datos
    #El segundo campo es el valor que se muestra al usuario

class Empleado(models.Model):
        nombre_empleado = models.CharField(max_length=200)
        #Nombre de empleado, tipo char, longitud máxima 200
        apellido_empleado = models.CharField(max_length=100)
        email_empleado = models.EmailField(max_length=50, unique=True)
        #Email de empleado, tipo email, longitud máxima 50
        edad_empleado = models.IntegerField()
        #Edad de empleado, tipo entero
        genero_empleado = models.CharField(max_length=80, choices=GENERO_OPCIONES)
        #Genero de empleado, tipo char, longitud máxima 80, opciones de genero
        salario_empleado = models.IntegerField(null=False, blank=False)
        #Salario de empleado, tipo entero, no nulo, no vacío
        fecha_registro = models.DateTimeField(auto_now_add=True, null=True, blank=True)
        #Fecha de registro, se establece automaticamente en fecha y hora actual al crear un registro
        ultima_modificacion = models.DateTimeField(auto_now=True)
        #Ultima modificación, se establece automaticamente en fecha y hora actual al modificar un registro