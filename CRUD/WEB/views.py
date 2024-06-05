from django.shortcuts import render, redirect, get_object_or_404
from .models import Empleado, Departamento  # Importa el modelo Departamento
from .forms import EmpleadoForm, DepartamentoForm  # Importa el formulario DepartamentoForm

def registrar_departamento(request):  # Nueva vista para registrar departamentos
    if request.method == "POST":
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_departamento')  # Redirige a la nueva vista listar_departamento
    else:
        form = DepartamentoForm()
    return render(request, 'registrar_departamento.html', {'form': form})

def listar_departamento(request):  # Nueva vista para listar departamentos
    departamentos = Departamento.objects.all()
    return render(request, 'listar_departamento.html', {'departamentos': departamentos})

def registrar_empleado(request): 
    if request.method == "POST":
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_empleado')
    else:
        form = EmpleadoForm()
    return render(request, 'registrar_empleado.html', {'form': form})

def listar_empleado(request):
    empleados = Empleado.objects.all()
    return render(request, 'listar_empleado.html', {'empleados': empleados})

def actualizar_empleado(request, id):
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