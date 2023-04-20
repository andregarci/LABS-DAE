from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    def __str__(self):
        return self.nombre
class Producto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    stock = models.IntegerField(default=0)
    pub_date = models.DateField('date published')
    def __str__(self):
        return self.nombre
class Cliente(models.Model):
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    dni = models.IntegerField()
    telefono = models.IntegerField(max_length=15)
    direccion = models.CharField(max_length=100)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    fecha_publicacion = models.DateTimeField()

    def __str__(self):
        return self.apellidos
