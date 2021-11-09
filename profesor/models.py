from django.db import models

# Create your models here.
from grupo.models import Grupo
from instituciones.models import Institucion
from materias.models import Materia


class Profesor(models.Model):
    nombres = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    correo = models.CharField(max_length=100)
    telefono = models.CharField(max_length=30)
    fecha_registro = models.DateField(auto_now_add=True)
    institucion = models.ForeignKey(
        Institucion,
        on_delete=models.SET_NULL,
        null = True,
        related_name='profesores',
    )
    materia = models.ForeignKey(
        Materia,
        on_delete=models.SET_NULL,
        null=True,
        related_name='profesores',
    )
    Grupos = models.ManyToManyField(Grupo, related_name='profesores')


    def __str__(self):
        return f'{self.nombres} {self.apellidos} | {self.institucion}'