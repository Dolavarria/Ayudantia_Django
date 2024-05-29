from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm

def registrar_empleado(request): 
    #Si se recibe un metodo post(Se envia el formulario)
    if request.method == "POST":
        #Creamos un formulario con los datos recibidos
        form = EmpleadoForm(request.POST)
        #Si el formulario es valido, es decir pasa las validaciones del modelo
        if form.is_valid():
            #Guardamos el formulario
            form.save()
            #Redirigimos a la lista de empleados
            return redirect('listar_empleado')
    #Si no se recibe un metodo post
    else:
        #Creamos un formulario vacio
        form = EmpleadoForm()
        #return render usa el archivo registrar_empleado.html y le pasa el formulario
    return render(request, 'registrar_empleado.html', {'form': form})

def listar_empleado(request):
    #Obtenemos todos los empleados
    empleados = Empleado.objects.all()
    #return render usa el archivo listar_empleados.html y le pasa los empleados
    return render(request, 'listar_empleado.html', {'empleados': empleados})

def actualizar_empleado(request, id):
    #Obtenemos el empleado con el id recibido
    #lo que get_object_or_404 hace es buscar un objeto en la base de datos
    empleado = get_object_or_404(Empleado, id=id)
    if request.method == "POST":
        form = EmpleadoForm(request.POST, instance=empleado)
        if form.is_valid():
            form.save()
            return redirect('listar_empleado')
    else:
        form = EmpleadoForm(instance=empleado)
    return render(request, 'actualizar_empleado.html', {'form': form})

def eliminar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect('listar_empleado')