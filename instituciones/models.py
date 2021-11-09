from django.db import models

# Create your models here.
class Institucion(models.Model):
    nombres = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=50)
    pais = models.CharField(max_length=30)
    telefono = models.CharField(max_length=30)
    fecha_registro = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombres} | {self.ciudad}, {self.pais}'
