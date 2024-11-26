from django.shortcuts import render,redirect 
from .models import Empleados
# Create your views here.

def inicio_vistaEmpleados(request):
    losempleados=Empleados.objects.all()
    return render(request,"gestionarEmpleados.html",{"misempleados":losempleados})

def registrarEmpleado(request):
    id_empleado=request.POST["txtempleado"]
    nombre=request.POST["txtnombre"]
    cargo=request.POST["txtcargo"]
    email=request.POST["txtemail"]
    telefono=request.POST["txttelefono"]
    salario=request.POST["txtsalario"]
    id_sucursales=request.POST["txtsucursales"]
    

    guardarempleados=Empleados.objects.create(
        id_empleado=id_empleado,nombre=nombre,cargo=cargo,email=email,telefono=telefono,salario=salario,id_sucursales=id_sucursales
    ) # GUARDA EL REGISTRO

    return redirect("empleado")

def seleccionarEmpleado(request,id_empleado):
    empleado=Empleados.objects.get(id_empleado=id_empleado)
    return render(request,"editarempleado.html",{"misempleados":empleado})

def editarEmpleado(request):
    id_empleado=request.POST["txtempleado"]
    nombre=request.POST["txtnombre"]
    cargo=request.POST["txtcargo"]
    email=request.POST["txtemail"]
    telefono=request.POST["txttelefono"]
    salario=request.POST["txtsalario"]
    id_sucursales=request.POST["txtsucursales"]
    empleado=Empleados.objects.get(id_empleado=id_empleado)
    empleado.nombre=nombre
    empleado.cargo=cargo
    empleado.email=email
    empleado.telefono=telefono
    empleado.salario=salario
    empleado.id_sucursales=id_sucursales
    empleado.save() # GUARDA EL REGISTRO
    return redirect("empleado")

def borrarEmpleado (request,id_empleado):
    empleado=Empleados.objects.get(id_empleado=id_empleado)
    empleado.delete() # ELIMINA EL REGISTRO
    return redirect("empleado")