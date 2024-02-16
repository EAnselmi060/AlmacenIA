from django.db import models

# Create your models here.
from django.db import models

class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    cantidad = models.PositiveIntegerField()

    class Meta:
        db_table = 'Producto'

class Admin(models.Model):
    cedula = models.CharField(primary_key=True, max_length=20)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)

    class Meta:
        db_table = 'Admin'

class HistorialProducto(models.Model):
    id_historial_producto = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    descripcion = models.TextField()

    class Meta:
        db_table = 'Historial_producto'

class HistorialAdmin(models.Model):
    id_historial_admin = models.AutoField(primary_key=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    descripcion = models.TextField()

    class Meta:
        db_table = 'Historial_admin'
