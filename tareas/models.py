from django.db import models

# Create your models here.
from materias.models import Materia


class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripción = models.CharField(max_length=1500)
    entregada = models.BooleanField(default=False)
    calificacion = models.FloatField(default=0.0)
    fecha_entrega = models.DateTimeField(blank=True, null=True)
    fecha_vencimiento = models.DateTimeField()
    fecha_registro = models.DateField(auto_now_add=True)
    materia = models.ForeignKey(
        Materia,
        on_delete=models.SET_NULL,
        null=True,
        related_name='tareas',
    )

    def __str__(self):
        return f'{self.titulo} | {self.fecha_vencimiento}'