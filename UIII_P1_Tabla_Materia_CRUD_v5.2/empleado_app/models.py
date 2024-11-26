from django.db import models

# Create your models here.
class Empleados(models.Model):
    id_empleado=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    cargo=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    telefono=models.CharField(max_length=100)
    salario=models.CharField(max_length=10)
    id_sucursales=models.CharField(max_length=6)
    


    def __str__(self):
        return self.nombre