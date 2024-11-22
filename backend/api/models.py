from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    numero = models.CharField(max_length=9)
    deudor = models.BooleanField()
   
    def __str__(self) -> str:
        return self.nombre + " " + self.apellido

class Usuario(models.Model):
    usuario = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    clave = models.CharField(max_length=100)

class Productos(models.Model):
    nombre = models.CharField(max_length=100)
    stock = models.IntegerField()
    precio = models.FloatField()
    estado = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nombre

class Ventas(models.Model):
    cantProductos = models.IntegerField()
    precioTotal = models.FloatField()
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    
class Boleta(models.Model):
    fechaHora = models.DateTimeField()
    pagado = models.BooleanField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    venta = models.ForeignKey(Ventas, on_delete=models.CASCADE)

class Pago(models.Model):
    medioPago = models.CharField(max_length=50)
    precio = models.FloatField()
    boleta = models.ForeignKey(Boleta, on_delete=models.CASCADE)
