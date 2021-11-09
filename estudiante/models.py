from django.db import models

# Create your models here.
#from grupo.models import Grupo
from instituciones.models import Institucion


class Estudiante(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30)
    acudiente = models.CharField(max_length=200)
    correo_acudiente = models.CharField(max_length=100)
    telefono_acudiente = models.CharField(max_length=30)
    fecha_registro = models.DateField(auto_now_add=True)
    institucion = models.ForeignKey(
        Institucion,
        on_delete=models.SET_NULL,
        null = True,
        related_name='estudiantes',
    )
    #Grupos = models.OneToOneField(Grupo, related_name='grupo')

    def __str__(self):
        return f'{self.nombres} {self.apellidos} | {self.institucion}'