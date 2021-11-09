from django.db import models

# Create your models here.
from grupo.models import Grupo


class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    fecha_registro = models.DateField(auto_now_add=True)
    grupo = models.ForeignKey(
        Grupo,
        on_delete=models.SET_NULL,
        null=True,
        related_name='clases',
    )

    def __str__(self):
        return f'{self.nombre} | {self.grupo.nombre}'