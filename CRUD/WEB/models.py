from django.db import models

# Create your models here.
#Crearemos una nueva tabla para aplicar FK
class Departamento(models.Model):
    nombre_departamento = models.CharField(max_length=200)
    ubicacion= models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre_departamento
        #retorna el nombre del departamento




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
        
        #para vincular la tabla Departamento con la tabla Empleado
        departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
        #django identifica que la tabla Departamento es la tabla padre y la tabla Empleado es la tabla hija
        #on_delete=models.CASCADE, si se elimina un registro de la tabla padre, se eliminan todos los registros de la tabla hija
        #django por si solo identifica cual es la primary key de la tabla padre y la vincula con la tabla hija
