from django.db import models

# Create your models here.
class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    grado = models.CharField(max_length=10)
    fecha_registro = models.DateField(auto_now_add=True)


    def __str__(self):
        return f'{self.nombre} | {self.grado}'
