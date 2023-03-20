from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30) 
    direccion=models.CharField(max_length=30)
    correo= models.EmailField(blank=True, null=True)
    telefono=models.CharField(max_length=7)

    def __str__(self):
        return self.nombre


class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=30)
    precio= models.IntegerField()

    
class pedidos(models.Model):
    telefono=models.CharField(max_length=7)
    fecha=models.DateField()
    entregado=models.BooleanField()
