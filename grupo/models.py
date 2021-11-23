from django.db import models

# Create your models here.
from estudiante.models import Estudiante
#from profesor.models import Profesor
from tareas.models import Tarea


class Grupo(models.Model):
    nombre = models.CharField(max_length=100)
    grado = models.CharField(max_length=10)
    cantidad_alumnos = models.IntegerField()
    fecha_registro = models.DateField(auto_now_add=True)
    tareas = models.ForeignKey(
        Tarea,
        on_delete=models.SET_NULL,
        null=True,
        related_name='grupos',
    )
    estudiantes = models.OneToOneField(
        Estudiante,
        on_delete=models.SET_NULL,
        null=True,
        related_name='grupo',
    )
    #tareas = models.ManyToManyField(Profesor, related_name='profesores')


    def __str__(self):
        return f'{self.nombre} | {self.grado}'