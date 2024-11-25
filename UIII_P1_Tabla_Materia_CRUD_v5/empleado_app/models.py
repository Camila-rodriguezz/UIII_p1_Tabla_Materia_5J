from django.db import models

# Create your models here.
class Empleados(models.Model):
    id_empleado=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    curp=models.CharField(max_length=100)
    acta_de_nacimiento=models.CharField(max_length=100)
    numero_celular=models.CharField(max_length=10)
    rfc=models.CharField(max_length=100)
    id_sucursales=models.CharField(max_length=6)
    direccion=models.CharField(max_length=100)


    def __str__(self):
        return self.nombre